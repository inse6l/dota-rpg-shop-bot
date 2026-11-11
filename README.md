# dota-rpg-shop-bot
Modular Telegram RPG Bot inspired by Dota 2 item shop, crafting system, quizzes, and SQLite database.
# 🏪 Dota 2 Secret Shop — Telegram RPG Bot (v1.0)

A modular Telegram bot written in Python (`pyTelegramBotAPI`) featuring an RPG economy, multi-tier item crafting, dynamic hero stats calculation, interactive quizzes, and persistent storage via SQLite.

## 🚀 Key Features (v1.0 MVP)
* **Modular Architecture:** Clean separation of concerns across `tg_lavka.py` (bot logic & UI), `game_data.py` (items, recipes, quizzes), and `database.py` (SQLite persistence).
* **Dynamic Combat Power (Power Score):** Real-time calculation of Damage, Magic Damage, Attack Speed, Armor (with physical resistance formula), Magic Resistance, and Attributes.
* **Smart Auto-Crafting & Inventory:** 10-slot inventory limit with automatic recipe detection and 18 multi-tier craftable artifacts.
* **Interactive Quiz System:** Earn gold by answering 20 curated questions based on Patch 7.41f and The International 2026.
* **Role-Based Access:** Admin commands for instant balance testing and unlimited inventory slots.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Framework:** pyTelegramBotAPI (telebot)
* **Database:** SQLite3
* **Hosting:** PythonAnywhere (24/7 Cloud Deployment)

## 🗺️ Roadmap
- [x] **v1.0:** Core shop, crafting, dynamic stats, quiz economy, and SQLite integration.
- [ ] **v2.0:** Hero class selection (Carry / Mid) with unique innate passives and stamina system.
- [ ] **v3.0:** PvE Dungeons & Boss raids with rare upgrade recipes.
- [ ] **v4.0:** Migration to Telegram Mini App (WebApp) with custom visual UI.
