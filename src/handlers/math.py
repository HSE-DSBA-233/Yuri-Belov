from aiogram import Router, types, F
from aiogram.filters import Command
from utils.logging import handler
from keyboards.inline.math import InlineKeyboards
from filters.chat_type import ChatTypeFilter

math_router = Router(name='math')
math_router.message.filter(ChatTypeFilter(chat_type=["private"]))

@math_router.message(F.text == "Математика")
async def math_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer("Выберите раздел:", reply_markup=InlineKeyboards().math_menu())


# callback on theory button from, math menu
@math_router.callback_query(F.data == "math_theory")
async def programming_theory_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Теория", reply_markup=InlineKeyboards().math_theory())


# callback on theory button from, math menu
@math_router.callback_query(F.data == "math_tasks")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Задачи", reply_markup=InlineKeyboards().math_tasks())


# callback on history button from, math menu
@math_router.callback_query(F.data == "math_history")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="История", reply_markup=InlineKeyboards().math_history())

