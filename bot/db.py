import json
import os

DB_FILE = "salon.json"


def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def add_booking(entry):
    data = load_db()
    entry["id"] = len(data) + 1
    data.append(entry)
    save_db(data)