"""
Start Command Handler Module.

This module contains a handler for the /start command. It responds with a welcome message and an inline keyboard
in private chats.

Functions:
    start_handler: Handles the /start command by sending a welcome message and an inline keyboard.
"""

from aiogram import Router, types, F
from aiogram.filters import Command
from utils.logging import handler
from keyboards.inline.start import InlineKeyboards
from filters.chat_type import ChatTypeFilter

start_router = Router(name='start')
start_router.message.filter(ChatTypeFilter(chat_type=["private"]))


@start_router.message(Command(commands='start'))
async def start_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="Меню:", reply_markup=InlineKeyboards().start())

# Возврат в стартовое меню по кнопке "Назад" из разделов "Math", "Programming", etc
@start_router.callback_query(F.data == "start")
async def start_menu_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Меню:", reply_markup=InlineKeyboards().start())

# Раздел "О боте"
@start_router.callback_query(F.data == "about")
async def start_about_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="О боте.", reply_markup=InlineKeyboards().start_about())
