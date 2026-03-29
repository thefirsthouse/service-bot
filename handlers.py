from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import ADMIN_ID
from aiogram import Bot

router = Router()


user_data = {}

services = {
    "cut": "Стрижка",
    "shave": "Бритье",
    "full": "Комплекс"
}


@router.message(CommandStart())
async def start(message: Message):

    kb = InlineKeyboardBuilder()

    kb.button(text="Стрижка", callback_data="service_cut")
    kb.button(text="Бритье", callback_data="service_shave")
    kb.button(text="Комплекс", callback_data="service_full")

    kb.adjust(1)

    await message.answer(
        "Здравствуйте!\nВыберите услугу",
        reply_markup=kb.as_markup()
    )


@router.callback_query(F.data.startswith("service"))
async def choose_service(callback: CallbackQuery):

    service = callback.data.split("_")[1]

    user_data[callback.from_user.id] = {"service": service}

    kb = InlineKeyboardBuilder()

    kb.button(text="12:00", callback_data="time_12")
    kb.button(text="14:00", callback_data="time_14")
    kb.button(text="16:00", callback_data="time_16")
    kb.button(text="18:00", callback_data="time_18")

    kb.adjust(2)

    await callback.message.edit_text(
        "Выберите время",
        reply_markup=kb.as_markup()
    )

    await callback.answer()


@router.callback_query(F.data.startswith("time"))
async def choose_time(callback: CallbackQuery, bot: Bot):

    user_id = callback.from_user.id

    
    if user_id in user_data and user_data[user_id].get("booked"):
        await callback.message.answer("❌ Вы уже записаны")
        await callback.answer()
        return

    time = callback.data.split("_")[1]

    data = user_data.get(user_id)

    if not data:
        await callback.message.answer("Ошибка, начните заново через /start")
        return

    service = services[data["service"]]

    username = callback.from_user.username
    username_text = f"@{username}" if username else "нет username"

    
    user_data[user_id]["time"] = time
    user_data[user_id]["booked"] = True   # <-- ВАЖНО

    text = f"""
✅ Запись подтверждена

Услуга: {service}
Время: {time}:00
"""

    await callback.message.answer(text)

    admin_text = f"""
🔥 Новая запись

Имя: {callback.from_user.first_name}
Username: @{username_text}

Услуга: {service}
Время: {time}:00
"""

    await bot.send_message(ADMIN_ID, admin_text)

    await callback.answer()
