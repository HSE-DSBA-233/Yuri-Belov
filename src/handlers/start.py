"""
Start Command Handler Module.

This module contains a handler for the /start command. It responds with a welcome message and an inline keyboard
in private chats.

Functions:
    start_handler: Handles the /start command by sending a welcome message and an inline keyboard.
"""

from aiogram import Router, types
from aiogram.filters import Command
from utils.logging import handler
from keyboards.inline.start import InlineKeyboards
from filters.chat_type import ChatTypeFilter

start_router = Router(name='start')
start_router.message.filter(ChatTypeFilter(chat_type=["private"]))


@start_router.message(Command(commands='start'))
async def start_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="<b>Добро пожаловать в бот советской математики и программирования!</b>", reply_markup=InlineKeyboards().start())
