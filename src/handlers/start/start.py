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
from keyboards.default.start import DefaultKeyboards
from filters.chat_type import ChatTypeFilter

start_router = Router(name='start')
start_router.message.filter(ChatTypeFilter(chat_type=["private"]))


@start_router.message(Command(commands='start'))
async def start_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="<b>Welcome to the Sovetsky Bot!</b>\n\nChoose from the menu below:", 
                         reply_markup=DefaultKeyboards().start_default_keyboard(),
                         parse_mode="HTML")


# Раздел "О боте"
@start_router.message(F.text == "About")
async def start_about_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="Bot was created by HSE DSBA 233 students-geeks in honor of the ORG project!")
