import telebot
from telebot import types
import random
from game_data import MAX_BAG_SLOTS, catalog, crafted_items, recipes, quizzes
from database import init_db, load_user, save_user
init_db()


BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
bot = telebot.TeleBot(BOT_TOKEN)
ADMIN_ID = 123456789

users_data = {}

# Словарь красивых названий характеристик
stat_labels = {
    "dmg": "⚔️ Урон",
    "mag_dmg": "🔮 Маг. урон",
    "as": "⚡ Скор. атаки",
    "armor": "🛡️ Броня",
    "mag_res": "💠 Маг. сопр.",
    "str": "💪 Сила",
    "agi": "🏃 Ловкость",
    "int": "🧠 Интеллект",
    "ms": "👟 Скор. бега"
}

def format_stats_inline(stats_dict):
    if not stats_dict:
        return "Свиток сборки"
    parts = []
    for k, v in stats_dict.items():
        if k == "mag_res":
            parts.append(stat_labels[k] + " +" + str(v) + "%")
        else:
            parts.append(stat_labels[k] + " +" + str(v))
    return ", ".join(parts)

def get_item_info(item_key):
    for cat in catalog.values():
        if item_key in cat["items"]:
            return cat["items"][item_key]
    if item_key in crafted_items:
        return crafted_items[item_key]
    return {"name": item_key, "price": 0, "stats": {}}

def can_craft(target, bag):
    temp_bag = bag.copy()
    for part in recipes[target]:
        if part in temp_bag:
            temp_bag.remove(part)
        else:
            return False
    return True

# Подсчет всех статов и общей Боевой Мощи (Power Score) героя
def calculate_hero_stats(bag):
    totals = {"dmg": 0, "mag_dmg": 0, "as": 0, "armor": 0, "mag_res": 25, "str": 20, "agi": 20, "int": 20, "ms": 300}
    for item_key in bag:
        stats = get_item_info(item_key).get("stats", {})
        for k, v in stats.items():
            totals[k] = totals.get(k, 0) + v

    # Расчет физического сопротивления от брони (формула Dota 2)
    armor = totals["armor"]
    phys_res = round((0.06 * armor) / (1 + 0.06 * abs(armor)) * 100, 1)

    # Формула общей боевой мощи для будущих данжей и боссов
    power_score = int(
        totals["dmg"] * 3 +
        totals["mag_dmg"] * 2.5 +
        totals["as"] * 2 +
        totals["armor"] * 12 +
        (totals["mag_res"] - 25) * 8 +
        (totals["str"] + totals["agi"] + totals["int"]) * 4
    )
    return totals, phys_res, power_score

active_quizzes = {}

def get_user(user_id):
    return load_user(user_id)


def main_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🏪 Магазин"), types.KeyboardButton("🎒 Рюкзак и Статы"))
    markup.add(types.KeyboardButton("⚔️ Задания (Фарм)"), types.KeyboardButton("⚒️ Рецепты"))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = get_user(message.from_user.id)
    text = (
        "👋 Добро пожаловать в Потайную Лавку v6.0 (Патч 7.41f)!\n\n"
        "💰 Твой капитал: " + str(user["gold"]) + " золота.\n"
        "🎒 Вместимость рюкзака: " + str(MAX_BAG_SLOTS) + " слотов.\n"
        "• Покупай боевые предметы в 🏪 Магазине\n"
        "• Собирай артефакты в ⚒️ Рецептах\n"
        "• Следи за Боевой Мощью в 🎒 Рюкзаке"
    )
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user = get_user(message.from_user.id)
    text = message.text.strip()
        # СЕКРЕТНАЯ АДМИН-КОМАНДА: /gold 50000
    if text.startswith("/gold") and message.from_user.id == ADMIN_ID:
        parts = text.split()
        if len(parts) == 2 and parts[1].isdigit():
            amount = int(parts[1])
            user["gold"] += amount
            user["gold"] += amount
            save_user(user)

            bot.send_message(message.chat.id, "👑 [АДМИН] Начислено +" + str(amount) + " золота. Баланс: " + str(user["gold"]) + "💰")
        else:
            bot.send_message(message.chat.id, "👑 Пиши так: /gold 50000")
        return


    if text == "🏪 Магазин":
        markup = types.InlineKeyboardMarkup(row_width=2)
        for cat_key, cat_data in catalog.items():
            markup.add(types.InlineKeyboardButton(cat_data["title"], callback_data="cat_" + cat_key))
        msg = "🏪 Выбери отдел лавки:\n💰 Баланс: " + str(user["gold"]) + " | 🎒 Слоты: " + str(len(user["bag"])) + "/" + str(MAX_BAG_SLOTS)
        bot.send_message(message.chat.id, msg, reply_markup=markup)

    elif text == "🎒 Рюкзак и Статы":
        totals, phys_res, power_score = calculate_hero_stats(user["bag"])

        stats_block = (
            "📊 ХАРАКТЕРИСТИКИ ГЕРОЯ:\n"
            "🔥 БОЕВАЯ МОЩЬ (POWER): " + str(power_score) + "\n"
            "━━━━━━━━━━━━━━━\n"
            "⚔️ Урон: " + str(totals["dmg"]) + " | 🔮 Маг. урон: +" + str(totals["mag_dmg"]) + "\n"
            "⚡ Скор. атаки: +" + str(totals["as"]) + " | 👟 Скорость: " + str(totals["ms"]) + "\n"
            "🛡️ Броня: " + str(totals["armor"]) + " (Физ. защита: " + str(phys_res) + "%)\n"
            "💠 Маг. сопротивление: " + str(totals["mag_res"]) + "%\n"
            "💪 Сила: " + str(totals["str"]) + " | 🏃 Ловкость: " + str(totals["agi"]) + " | 🧠 Инт: " + str(totals["int"]) + "\n"
            "━━━━━━━━━━━━━━━\n"
        )

        if not user["bag"]:
            bot.send_message(message.chat.id, stats_block + "🎒 Рюкзак пуст (0/" + str(MAX_BAG_SLOTS) + " слотов).\n💰 Баланс: " + str(user["gold"]) + " золота.")
            return

        markup = types.InlineKeyboardMarkup(row_width=1)
        for target in recipes.keys():
            if can_craft(target, user["bag"]):
                target_name = get_item_info(target)["name"]
                markup.add(types.InlineKeyboardButton("⚡ СОБРАТЬ: " + target_name.upper() + "!", callback_data="craft_" + target))

        bag_display = []
        unique_items = list(set(user["bag"]))
        for item_key in unique_items:
            info = get_item_info(item_key)
            count = user["bag"].count(item_key)
            bag_display.append("• " + info["name"] + " (x" + str(count) + ")")
            sell_price = int(info["price"] / 2)
            markup.add(types.InlineKeyboardButton("💵 Продать " + info["name"] + " (+" + str(sell_price) + "💰)", callback_data="sell_" + item_key))

        reply = stats_block + "🎒 ИНВЕНТАРЬ (" + str(len(user["bag"])) + "/" + str(MAX_BAG_SLOTS) + " слотов):\n" + "\n".join(bag_display) + "\n\n💰 Баланс: " + str(user["gold"]) + " золота"
        bot.send_message(message.chat.id, reply, reply_markup=markup)

    elif text == "⚔️ Задания (Фарм)":
        quiz = random.choice(quizzes)
        active_quizzes[message.from_user.id] = quiz
        markup = types.InlineKeyboardMarkup(row_width=1)
        for idx, opt in enumerate(quiz["options"]):
            markup.add(types.InlineKeyboardButton(opt, callback_data="quiz_" + str(idx)))

        reply = (
            "⚔️ ВИКТОРИНА ПАТЧА 7.41f И TI 2026\n"
            "Награда за верный ответ: +" + str(quiz["reward"]) + " золота\n\n"
            "❓ " + quiz["q"]
        )
        bot.send_message(message.chat.id, reply, reply_markup=markup)

    elif text == "⚒️ Рецепты":
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for target in recipes.keys():
            target_info = get_item_info(target)
            prefix = "✅ " if can_craft(target, user["bag"]) else "🔸 "
            buttons.append(types.InlineKeyboardButton(prefix + target_info["name"], callback_data="viewrec_" + target))
        markup.add(*buttons)
        bot.send_message(message.chat.id, "⚒️ КНИГА РЕЦЕПТОВ (Нажми на артефакт, чтобы увидеть состав и статы):", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user = get_user(call.from_user.id)
    data = call.data

    if data.startswith("cat_"):
        cat_key = data.replace("cat_", "")
        cat_data = catalog[cat_key]
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        items_desc = []

        for item_key, item_info in cat_data["items"].items():
            stats_text = format_stats_inline(item_info.get("stats", {}))
            items_desc.append("• " + item_info["name"] + " (" + str(item_info["price"]) + "💰) — " + stats_text)
            buttons.append(types.InlineKeyboardButton(item_info["name"] + " (" + str(item_info["price"]) + "💰)", callback_data="buy_" + item_key))

        markup.add(*buttons)
        markup.add(types.InlineKeyboardButton("⬅️ Назад к отделам", callback_data="back_to_shop"))

        header = "📂 " + cat_data["title"] + "\n💰 Баланс: " + str(user["gold"]) + " | 🎒 Слоты: " + str(len(user["bag"])) + "/" + str(MAX_BAG_SLOTS) + "\n\n"
        bot.answer_callback_query(call.id)
        bot.edit_message_text(header + "\n".join(items_desc), call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif data == "back_to_shop":
        markup = types.InlineKeyboardMarkup(row_width=2)
        for cat_key, cat_data in catalog.items():
            markup.add(types.InlineKeyboardButton(cat_data["title"], callback_data="cat_" + cat_key))
        bot.answer_callback_query(call.id)
        msg = "🏪 Выбери отдел лавки:\n💰 Баланс: " + str(user["gold"]) + " | 🎒 Слоты: " + str(len(user["bag"])) + "/" + str(MAX_BAG_SLOTS)
        bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif data.startswith("buy_"):
        is_admin = (call.from_user.id == ADMIN_ID)

        if not is_admin and len(user["bag"]) >= MAX_BAG_SLOTS:
            bot.answer_callback_query(call.id, "🎒 Рюкзак переполнен (10/10)! Скрафти или продай лишнее.", show_alert=True)
            return

        item_key = data.replace("buy_", "")
        info = get_item_info(item_key)

        if is_admin:
            user["bag"].append(item_key)
            save_user(user)
            bot.answer_callback_query(call.id, "👑 [АДМИН] Взято бесплатно: " + info["name"] + " | Слотов: " + str(len(user["bag"])))
        elif user["gold"] >= info["price"]:
            user["gold"] -= info["price"]
            user["bag"].append(item_key)
            save_user(user)
            bot.answer_callback_query(call.id, "✅ Куплено: " + info["name"] + " | Слоты: " + str(len(user["bag"])) + "/10")
        else:
            bot.answer_callback_query(call.id, "❌ Не хватает золота! Нужно " + str(info["price"]), show_alert=True)

    elif data.startswith("viewrec_"):
        target = data.replace("viewrec_", "")
        target_info = get_item_info(target)
        needed = recipes[target]

        temp_bag = user["bag"].copy()
        parts_status = []
        for part in needed:
            p_name = get_item_info(part)["name"]
            if part in temp_bag:
                temp_bag.remove(part)
                parts_status.append("✅ " + p_name + " (есть в сумке)")
            else:
                parts_status.append("❌ " + p_name + " (нужно купить)")

        stats_str = format_stats_inline(target_info.get("stats", {}))
        text = (
            "⚒️ ЧЕРТЕЖ: " + target_info["name"].upper() + "\n"
            "📊 Бонусы предмета: " + stats_str + "\n\n"
            "Необходимые компоненты:\n" + "\n".join(parts_status)
        )
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("🔥 СОБРАТЬ " + target_info["name"].upper(), callback_data="craft_" + target))
        markup.add(types.InlineKeyboardButton("⬅️ Назад к списку рецептов", callback_data="back_to_recipes"))
        bot.answer_callback_query(call.id)
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif data == "back_to_recipes":
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = []
        for target in recipes.keys():
            target_info = get_item_info(target)
            prefix = "✅ " if can_craft(target, user["bag"]) else "🔸 "
            buttons.append(types.InlineKeyboardButton(prefix + target_info["name"], callback_data="viewrec_" + target))
        markup.add(*buttons)
        bot.answer_callback_query(call.id)
        bot.edit_message_text("⚒️ КНИГА РЕЦЕПТОВ (Нажми на артефакт, чтобы увидеть состав и статы):", call.message.chat.id, call.message.message_id, reply_markup=markup)

    elif data.startswith("quiz_"):
        quiz = active_quizzes.get(call.from_user.id)
        if not quiz:
            bot.answer_callback_query(call.id, "Это задание уже завершено!")
            return

        chosen_idx = int(data.replace("quiz_", ""))
        chosen_answer = quiz["options"][chosen_idx]
        active_quizzes[call.from_user.id] = None

        if chosen_answer == quiz["answer"]:
            user["gold"] += quiz["reward"]
            save_user(user)
            result_text = "✅ ВЕРНО! Ответ: " + quiz["answer"] + "\n💰 Награда: +" + str(quiz["reward"]) + " золота\nТвой баланс: " + str(user["gold"]) + "💰"
        else:
            result_text = "❌ ОШИБКА! Твой ответ: " + chosen_answer + "\nПравильный ответ: " + quiz["answer"] + "\nНаграда не получена."

        bot.answer_callback_query(call.id)
        bot.edit_message_text(result_text, call.message.chat.id, call.message.message_id)

    elif data.startswith("sell_"):
        item_key = data.replace("sell_", "")
        if item_key in user["bag"]:
            info = get_item_info(item_key)
            refund = int(info["price"] / 2)
            user["bag"].remove(item_key)
            user["gold"] += refund
            save_user(user)
            bot.answer_callback_query(call.id, "💵 Продано за +" + str(refund) + " золота!")
            bot.delete_message(call.message.chat.id, call.message.message_id)
        else:
            bot.answer_callback_query(call.id, "Предмет уже продан!")

    elif data.startswith("craft_"):
        target = data.replace("craft_", "")
        needed = recipes[target]
        temp_bag = user["bag"].copy()

        for part in needed:
            if part in temp_bag:
                temp_bag.remove(part)
            else:
                part_name = get_item_info(part)["name"]
                bot.answer_callback_query(call.id, "⚠️ Не хватает: " + part_name, show_alert=True)
                return

        user["bag"] = temp_bag
        user["bag"].append(target)
        save_user(user)
        target_name = get_item_info(target)["name"]
        bot.answer_callback_query(call.id, "🔥 УСПЕХ! Собран артефакт: " + target_name + "!", show_alert=True)
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass

print("Бот v6.5 (База данных SQLite + Админка) запущен!")
bot.infinity_polling(timeout=20, long_polling_timeout=10)

