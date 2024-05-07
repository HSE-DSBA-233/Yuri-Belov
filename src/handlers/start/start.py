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
from aiogram.fsm.context import FSMContext
from data.config import conf
from loader import bot
from aiogram.filters import StateFilter
from handlers.chat.chat import chat
import re

start_router = Router(name='start')
start_router.message.filter(ChatTypeFilter(chat_type=["private"]))

with open("src/handlers/start/msg_templates/greet.txt") as f:
    GREET_MESSAGE = f.read()
    f.close()

with open("src/handlers/start/msg_templates/cyrillic_error.txt") as f:
    CYRILLIC_ERROR = f.read()
    f.close()

with open("src/handlers/start/msg_templates/about.txt") as f:
    ABOUT = f.read()
    f.close()

async def cyrillic(text): # checks if string has cyrillic symbols
    return bool(re.search('[а-яА-Я]', text))


@start_router.message(Command(commands='start'))
async def start_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    await state.clear()
    await message.answer(GREET_MESSAGE, 
                         reply_markup=DefaultKeyboards().start_default_keyboard(),
                         parse_mode="HTML")
    await chat.update_context(message.from_user.id,GREET_MESSAGE) 


# Раздел "О боте"
@start_router.message(F.text == "About")
async def start_about_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    await state.clear()
    await message.answer(ABOUT,
                         parse_mode="HTML")


@start_router.message(Command("clear_chat")) # should be pretty obvious
async def command_clear_chat_handler(message: types.Message) -> None:
    await chat.clear_chat(message.from_user.id)
    await message.answer("The context has been cleared! Yuri forgot your entire dialogue!")


@start_router.message(StateFilter(None), ~F.text.in_(["Programming", "Mathematics", "About"]))
async def chat_handler(message: types.Message) -> None: # handling general chat with Yuri AI
    try:
        user_id = message.from_user.id

        await chat.start_chat(user_id)

        await bot.send_chat_action(chat_id=user_id, action="typing")

        await chat.resize_context(user_id)

        if not await cyrillic(message.text): # only if there are no cyrillic symbols
            response = await chat.generate_response(user_id, message.text) # getting the response
            await chat.update_context(user_id, response)
        else:
            response = CYRILLIC_ERROR

        await message.answer(response, parse_mode="HTML") # sending it to the user

    except TypeError as e: # just in case something goes wrong
        print(e)
        await message.answer("There's been an error. Repeat your message again, please.")

from pathlib import Path
from aiogram.types import ContentType, File, Message

async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")

@start_router.message(content_types=[ContentType.VOICE])
async def voice_message_handler(message: Message):
    voice = await message.voice.get_file()
    path = "/files/voices"

    await handle_file(file=voice, file_name=f"{voice.file_id}.ogg", path=path)