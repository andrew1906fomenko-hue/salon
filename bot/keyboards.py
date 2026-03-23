from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from .config import WEB_APP_URL


def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(
                text="📅 Записаться",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]],
        resize_keyboard=True
    )