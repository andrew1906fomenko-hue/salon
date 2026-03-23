import json
from aiogram import Router, F
from aiogram.types import Message
from .db import add_booking, load_db
from .config import ADMIN_ID

router = Router()

@router.message(F.text == "/start")
async def start(msg: Message):
    from .keyboards import main_menu
    await msg.answer("Откройте приложение 👇", reply_markup=main_menu())


@router.message(F.web_app_data)
async def web_app_data(msg: Message):
    data = json.loads(msg.web_app_data.data)
    data["user_id"] = msg.from_user.id

    add_booking(data)

    await msg.answer(
        f"✅ Запись подтверждена\n\n"
        f"👤 {data['name']}\n"
        f"💇 {data['service']}\n"
        f"📅 {data['date']}\n"
        f"⏰ {data['time']}"
    )


@router.message(F.text == "/admin")
async def admin(msg: Message):
    if msg.from_user.id != ADMIN_ID:
        return

    data = load_db()

    if not data:
        await msg.answer("Нет записей")
        return

    text = "Записи:\n"
    for b in data:
        text += f"#{b['id']} {b['name']} {b['service']} {b['date']} {b['time']}\n"

    await msg.answer(text)
