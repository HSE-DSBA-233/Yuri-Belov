from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter

programming_router = Router(name='programming')
programming_router.message.filter(ChatTypeFilter(chat_type=["private"]))


@programming_router.callback_query(F.data == "programming")
async def programming_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выбери раздел:", reply_markup=InlineKeyboards().programming_menu())


@programming_router.callback_query(F.data == "programming_theory")
async def programming_theory_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Теория")


@programming_router.callback_query(F.data == "programming_tasks")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Задачи")


@programming_router.callback_query(F.data == "programming_translator")
async def programming_translator_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Переводчик")
