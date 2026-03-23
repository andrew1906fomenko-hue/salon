import os

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set!")

ADMIN_ID = 5249205025
WEB_APP_URL = "https://salon-2qs9.onrender.com/"