from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from utils.logging import handler
from aiogram.filters import StateFilter
from keyboards.inline.math import InlineKeyboards
from states.math_state import MathState
from filters.chat_type import ChatTypeFilter
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
import json
import random
from data.config import conf
from utils.db_math import db


math_router = Router(name='math')
math_router.message.filter(ChatTypeFilter(chat_type=["private"]))


# default keyboard on math
@math_router.message(F.text == "Math")
async def math_handler_menu(message: types.Message):
    handler(__name__, type=message)
    await message.answer("Choose section:", reply_markup=InlineKeyboards().math_menu())


# callback on math
@math_router.callback_query(F.data == "math")
async def math_handler_menu(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Choose section:", reply_markup=InlineKeyboards().math_menu())

