"""/start command handler."""

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
    await message.answer(text="<b>Добро пожаловать в бот советской математики и программирования!</b>", reply_markup=InlineKeyboards().start())
