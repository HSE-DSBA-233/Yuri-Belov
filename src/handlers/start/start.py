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
    await message.answer("<b>I am Yuri Belov.</b>", 
                         reply_markup=DefaultKeyboards().start_default_keyboard(),
                         parse_mode="HTML")


# Раздел "О боте"
@start_router.message(F.text == "About")
async def start_about_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer("<b>About:</b>\n\n" 
                         "Bot was created by HSE DSBA 233 students-geeks in honor of the ORG project: @pvlppv, @gurbanoffn, @makaroshh, @eeleecc",
                         parse_mode="HTML")


# @start_router.message(F.text)
# async def chat_handler(message: types.Message):
#     try:
#         await message.answer("Soon!")
#     except TypeError:
#         await message.answer("Hm, it appears that the message you've provided might not be entirely valid. Give it another go, this time with a slightly different approach.")
