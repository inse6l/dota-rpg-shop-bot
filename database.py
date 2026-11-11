import sqlite3
import json

DB_NAME = "players.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            gold INTEGER,
            bag TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT gold, bag FROM users WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    
    if row is None:
        gold = 1500
        bag = []
        cursor.execute("INSERT INTO users (user_id, gold, bag) VALUES (?, ?, ?)", (user_id, gold, json.dumps(bag)))
        conn.commit()
    else:
        gold = row[0]
        bag = json.loads(row[1])
        
    conn.close()
    return {"user_id": user_id, "gold": gold, "bag": bag}

def save_user(user):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    bag_str = json.dumps(user["bag"])
    cursor.execute("UPDATE users SET gold = ?, bag = ? WHERE user_id = ?", (user["gold"], bag_str, user["user_id"]))
    conn.commit()
    conn.close()
