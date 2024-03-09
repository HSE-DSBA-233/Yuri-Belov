from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from utils.logging import handler
from keyboards.inline.history import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.types import FSInputFile

history_router = Router(name='history')
history_router.message.filter(ChatTypeFilter(chat_type=["private"]))


# callback on history button from math menu
@history_router.callback_query(F.data == "history_math")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="История", reply_markup=InlineKeyboards().history_math())

