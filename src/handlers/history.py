"""/history command handler."""

from aiogram import Router, types, F
from aiogram.filters import Command
from utils.logging import handler
from keyboards.inline.start import InlineKeyboards
from filters.chat_type import ChatTypeFilter

history_router = Router(name='history')
history_router.message.filter(ChatTypeFilter(chat_type=["private"]))


@history_router.callback_query(F.data == "history")
async def start_callback_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.answer("History.")
