MAX_BAG_SLOTS = 10

catalog = {
    "stats_boots": {
        "title": "🥾 Атрибуты и Обувь",
        "items": {
            "branches": {"name": "Iron Branch", "price": 50, "stats": {"str": 1, "agi": 1, "int": 1}},
            "boots": {"name": "Boots of Speed", "price": 500, "stats": {"ms": 45}},
            "gloves": {"name": "Gloves of Haste", "price": 450, "stats": {"as": 15}},
            "belt": {"name": "Belt of Strength", "price": 450, "stats": {"str": 6}},
            "band": {"name": "Band of Elvenskin", "price": 450, "stats": {"agi": 6}},
            "robe": {"name": "Robe of the Magi", "price": 450, "stats": {"int": 6}},
            "blades": {"name": "Blades of Attack", "price": 450, "stats": {"dmg": 9}},
            "ogre_axe": {"name": "Ogre Axe", "price": 1000, "stats": {"str": 10}},
            "blade_alacrity": {"name": "Blade of Alacrity", "price": 1000, "stats": {"agi": 10}},
            "staff_wizardry": {"name": "Staff of Wizardry", "price": 1000, "stats": {"int": 10}}
        }
    },
    "weapons": {
        "title": "⚔️ Оружие и Урон",
        "items": {
            "broadsword": {"name": "Broadsword", "price": 1000, "stats": {"dmg": 15}},
            "claymore": {"name": "Claymore", "price": 1350, "stats": {"dmg": 20}},
            "mithril": {"name": "Mithril Hammer", "price": 1600, "stats": {"dmg": 24}},
            "javelin": {"name": "Javelin", "price": 1100, "stats": {"dmg": 10, "mag_dmg": 20}},
            "blitz": {"name": "Blitz Knuckles", "price": 1000, "stats": {"as": 35}},
            "demon_edge": {"name": "Demon Edge", "price": 2200, "stats": {"dmg": 40}},
            "hyperstone": {"name": "Hyperstone", "price": 2000, "stats": {"as": 60}},
            "sacred_relic": {"name": "Sacred Relic", "price": 3400, "stats": {"dmg": 55}}
        }
    },
    "armor_magic": {
        "title": "🛡️ Броня и Магия",
        "items": {
            "chainmail": {"name": "Chainmail", "price": 550, "stats": {"armor": 4}},
            "helm_iron": {"name": "Helm of Iron Will", "price": 975, "stats": {"armor": 6}},
            "platemail": {"name": "Platemail", "price": 1400, "stats": {"armor": 10}},
            "cloak": {"name": "Cloak", "price": 800, "stats": {"mag_res": 20}},
            "point_booster": {"name": "Point Booster", "price": 1200, "stats": {"str": 5, "agi": 5, "int": 5}},
            "ultimate_orb": {"name": "Ultimate Orb", "price": 2800, "stats": {"str": 15, "agi": 15, "int": 15}},
            "eaglesong": {"name": "Eaglesong", "price": 2800, "stats": {"agi": 25}},
            "reaver": {"name": "Reaver", "price": 2800, "stats": {"str": 25}},
            "mystic_staff": {"name": "Mystic Staff", "price": 2800, "stats": {"int": 25}},
            "talisman": {"name": "Talisman of Evasion", "price": 1300, "stats": {"armor": 3, "agi": 5}},
            "morbid_mask": {"name": "Morbid Mask", "price": 900, "stats": {"dmg": 10}}
        }
    },
    "recipes_scrolls": {
        "title": "📜 Свитки рецептов",
        "items": {
            "rec_midas": {"name": "Рецепт Midas", "price": 1250, "stats": {}},
            "rec_daedalus": {"name": "Рецепт Daedalus", "price": 1000, "stats": {}},
            "rec_mjollnir": {"name": "Рецепт Mjollnir", "price": 900, "stats": {}},
            "rec_radiance": {"name": "Рецепт Radiance", "price": 1350, "stats": {}},
            "rec_heart": {"name": "Рецепт Heart", "price": 1200, "stats": {}},
            "rec_shiva": {"name": "Рецепт Shivas Guard", "price": 650, "stats": {}},
            "rec_bkb": {"name": "Рецепт BKB", "price": 1450, "stats": {}},
            "rec_skadi": {"name": "Рецепт Skadi", "price": 1000, "stats": {}}
        }
    }
}

crafted_items = {
    "power_treads": {"name": "Power Treads", "price": 1400, "stats": {"ms": 50, "as": 25, "str": 10, "agi": 10, "int": 10}},
    "phase_boots": {"name": "Phase Boots", "price": 1400, "stats": {"ms": 50, "dmg": 22, "armor": 5}},
    "midas": {"name": "Hand of Midas", "price": 1700, "stats": {"as": 40}},
    "armlet": {"name": "Armlet of Mordiggian", "price": 2500, "stats": {"dmg": 35, "as": 25, "armor": 6, "str": 25}},
    "battlefury": {"name": "Battle Fury", "price": 2350, "stats": {"dmg": 55}},
    "desolator": {"name": "Desolator", "price": 3650, "stats": {"dmg": 65, "armor": 4}},
    "maelstrom": {"name": "Maelstrom", "price": 2700, "stats": {"dmg": 28, "mag_dmg": 45}},
    "mjollnir": {"name": "Mjollnir", "price": 5600, "stats": {"dmg": 35, "as": 95, "mag_dmg": 80}},
    "bkb": {"name": "Black King Bar", "price": 4050, "stats": {"str": 15, "dmg": 30, "mag_res": 50}},
    "mkb": {"name": "Monkey King Bar", "price": 4300, "stats": {"dmg": 55, "as": 45, "mag_dmg": 40}},
    "butterfly": {"name": "Butterfly", "price": 4100, "stats": {"agi": 35, "dmg": 30, "as": 35, "armor": 6}},
    "daedalus": {"name": "Daedalus", "price": 3200, "stats": {"dmg": 95}},
    "radiance": {"name": "Radiance", "price": 4750, "stats": {"dmg": 65, "mag_dmg": 60, "armor": 4}},
    "skadi": {"name": "Eye of Skadi", "price": 7800, "stats": {"str": 35, "agi": 35, "int": 35, "armor": 5}},
    "heart": {"name": "Heart of Tarrasque", "price": 5000, "stats": {"str": 50, "armor": 5}},
    "satanic": {"name": "Satanic", "price": 4700, "stats": {"str": 30, "dmg": 50, "armor": 4}},
    "shiva": {"name": "Shivas Guard", "price": 4850, "stats": {"int": 35, "armor": 16, "mag_dmg": 50}},
    "khanda": {"name": "Khanda", "price": 5000, "stats": {"dmg": 50, "str": 12, "agi": 12, "int": 12, "mag_dmg": 65}}
}
recipes = {
    "power_treads": ["boots", "gloves", "belt"],
    "phase_boots": ["boots", "blades", "chainmail"],
    "midas": ["gloves", "rec_midas"],
    "armlet": ["helm_iron", "gloves", "blades"],
    "battlefury": ["broadsword", "claymore"],
    "desolator": ["mithril", "mithril", "blades"],
    "maelstrom": ["mithril", "javelin"],
    "mjollnir": ["maelstrom", "hyperstone", "rec_mjollnir"],
    "bkb": ["ogre_axe", "mithril", "rec_bkb"],
    "mkb": ["demon_edge", "javelin", "blitz"],
    "butterfly": ["eaglesong", "talisman"],
    "daedalus": ["demon_edge", "rec_daedalus"],
    "radiance": ["sacred_relic", "rec_radiance"],
    "skadi": ["ultimate_orb", "ultimate_orb", "point_booster", "rec_skadi"],
    "heart": ["reaver", "ogre_axe", "rec_heart"],
    "satanic": ["reaver", "morbid_mask", "claymore"],
    "shiva": ["mystic_staff", "platemail", "rec_shiva"],
    "khanda": ["demon_edge", "ultimate_orb", "staff_wizardry"]
}

quizzes = [
    {"q": "С каким счетом завершился гранд-финал The International 2026 между Team Spirit и Team Vision?", "options": ["3:2 в пользу Team Spirit", "3:1 в пользу Team Spirit", "3:0 в пользу Team Spirit", "3:2 в пользу Team Vision"], "answer": "3:2 в пользу Team Spirit", "reward": 600},
    {"q": "Кто из новых игроков присоединился к Yatoro, Collapse и Larl в чемпионском составе Team Spirit на TI 2026?", "options": ["rue и not_me", "Mira и Satanic", "Save- и Nightfall", "Malr1ne и ATF"], "answer": "rue и not_me", "reward": 550},
    {"q": "Какую роль в составе Team Spirit на The International 2026 занял Ярослав «Miposhka» Найденов?", "options": ["Тренер команды", "Капитан и саппорт 5-й позиции", "Аналитик студии", "Менеджер состава"], "answer": "Тренер команды", "reward": 500},
    {"q": "В каком городе проходил турнир The International 2026 (TI15)?", "options": ["Шанхай (Китай)", "Копенгаген (Дания)", "Сиэтл (США)", "Эр-Рияд (Саудовская Аравия)"], "answer": "Шанхай (Китай)", "reward": 450},
    {"q": "Что произошло с системой аспектов (Facets) в глобальном патче 7.41 весной 2026 года?", "options": ["Система аспектов была полностью удалена из игры", "Добавили по 4 аспекта каждому герою", "Аспекты стали открываться только с 15 уровня", "Аспекты перенесли в нейтральные предметы"], "answer": "Система аспектов была полностью удалена из игры", "reward": 550},
    {"q": "Где теперь появляются Рошан и Терзатель (Tormentor) после изменений карты в патче 7.41?", "options": ["Рошан начинает в верхнем логове, а Терзатель — в нижнем ущелье", "Оба появляются строго по центру реки", "Рошан в нижнем логове, Терзатель на базе", "Они меняются местами каждые 5 минут"], "answer": "Рошан начинает в верхнем логове, а Терзатель — в нижнем ущелье", "reward": 600},
    {"q": "Какие режимы были убраны из соревновательного матчмейкинга в рамках обновления Summer Scrub 2026?", "options": ["Random Draft и Ranked Classic", "All Pick и Captains Mode", "Turbo и Single Draft", "Ability Draft и All Random"], "answer": "Random Draft и Ranked Classic", "reward": 500},
    {"q": "Какой новый герой-бард появился в пуле персонажей Dota 2?", "options": ["Largo", "Ringmaster", "Kez", "Puppet Master"], "answer": "Largo", "reward": 450},
    {"q": "Кем по лору и облику является герой Kez?", "options": ["Птицеподобный воин-самурай", "Древний лесной дух", "Механический голем из шахт", "Повелитель глубоководных тварей"], "answer": "Птицеподобный воин-самурай", "reward": 450},
    {"q": "На чем сфокусировался осенний патч 7.41f?", "options": ["На точечных исправлениях багов логова Рошана, предметов и способностей", "На полном изменении ландшафта карты", "На добавлении 5 новых героев", "На удалении нейтральных предметов"], "answer": "На точечных исправлениях багов логова Рошана, предметов и способностей", "reward": 500},
    {"q": "Как в патче 7.41 изменилась механика работы врожденных способностей (Innate abilities)?", "options": ["Они больше не масштабируются от уровней прокачки других способностей", "Их можно прокачивать за золото в лавке", "Они работают только в ночное время суток", "Они больше не работают у героев-универсалов"], "answer": "Они больше не масштабируются от уровней прокачки других способностей", "reward": 600},
    {"q": "Какое место заняла команда Team Yandex на турнире The International 2026?", "options": ["3-е место", "2-е место", "4-е место", "5-6 место"], "answer": "3-е место", "reward": 500},
    {"q": "Сколько раз за свою историю организация Team Spirit выигрывала The International к концу 2026 года?", "options": ["Три раза (2021, 2023 и 2026)", "Два раза (2021 и 2023)", "Четыре раза", "Один раз"], "answer": "Три раза (2021, 2023 и 2026)", "reward": 500},
    {"q": "Что происходит на миникарте после обновления лета 2026 года, когда игрок стакает лагерь крипов?", "options": ["Иконка лагеря обновляется и отображает наличие стака до зачистки", "Лагерь подсвечивается красным для врагов", "Над лагерем появляется таймер возрождения", "Иконка исчезает с миникарты"], "answer": "Иконка лагеря обновляется и отображает наличие стака до зачистки", "reward": 550},
    {"q": "Как изменилась покупка предметов через двойной клик или меню «Purchase Item» в 2026 году?", "options": ["Она теперь обходит защиту от байбека", "Она дает скидку 5% на свитки", "Предметы сразу падают в тайник на базе", "Она заблокирована во время драки"], "answer": "Она теперь обходит защиту от байбека", "reward": 600},
    {"q": "Куда были перемещены модификаторы клавиш для фильтрации взаимодействия с юнитами в настройках 2026 года?", "options": ["Из раздела Dota Labs в стандартные настройки горячих клавиш", "В консоль разработчика", "В настройки графики и интерфейса", "Их удалили из клиента игры"], "answer": "Из раздела Dota Labs в стандартные настройки горячих клавиш", "reward": 550},
    {"q": "Какая команда заняла 2-е место на The International 2026, уступив в гранд-финале Team Spirit?", "options": ["Team Vision (PARIVISION)", "Gaimin Gladiators", "Team Liquid", "Team Falcons"], "answer": "Team Vision (PARIVISION)", "reward": 500},
    {"q": "Сколько героев насчитывал официальный пул Dota 2 на момент выхода весеннего патча 7.41?", "options": ["126 героев", "124 героя", "128 героев", "130 героев"], "answer": "126 героев", "reward": 500},
    {"q": "Куда теперь отправляется курьер при Alt-клике на кнопку «Go to Secret Shop»?", "options": ["Во вражескую тайную лавку", "В ближайший аванпост", "К руне мудрости", "На фонтан союзников"], "answer": "Во вражескую тайную лавку", "reward": 550},
    {"q": "Какой предмет в патче 7.41f получил исправление бага с восстановлением здоровья при получении урона?", "options": ["Tranquil Boots", "Heart of Tarrasque", "Vanguard", "Eternal Shroud"], "answer": "Tranquil Boots", "reward": 500}
]
