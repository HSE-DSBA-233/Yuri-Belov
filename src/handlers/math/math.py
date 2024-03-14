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
    await message.answer("<b>Math:</b>\n\n"
                         "This is the math section, my dear friend! A magnificent haven where the wonders of numbers and equations come to life, guided by the wisdom of my Soviet heritage."
                         "Just for you, I've crafted these delightful buttons below to guide our mathematical journey, choose your desired destination swiftly:\n\n"
                         "<b>- History!</b> Join me in celebrating the illustrious past of mathematics, as we pay tribute to the groundbreaking achievements of our fellow Soviet mathematicians.\n"
                         "<b>- Theory!</b> Let's delve into the captivating world of Soviet mathematics specifics and areas! I promise it'll be more fun than counting the stripes on a Siberian tiger – and just as thrilling!\n"
                         "<b>- Tasks!</b> Roll up your sleeves and tackle intriguing mathematical challenges alongside me, as we exchange ideas and unravel the mysteries of numbers and patterns.",
                         reply_markup=InlineKeyboards().math_menu(),
                         parse_mode="HTML")


# callback on math
@math_router.callback_query(F.data == "math")
async def math_handler_menu(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Math:</b>\n\n"
                         "This is the math section, my dear friend! A magnificent haven where the wonders of numbers and equations come to life, guided by the wisdom of my Soviet heritage."
                         "Just for you, I've crafted these delightful buttons below to guide our mathematical journey, choose your desired destination swiftly:\n\n"
                         "<b>- History!</b> Join me in celebrating the illustrious past of mathematics, as we pay tribute to the groundbreaking achievements of our fellow Soviet mathematicians.\n"
                         "<b>- Theory!</b> Let's delve into the captivating world of Soviet mathematics specifics and areas! I promise it'll be more fun than counting the stripes on a Siberian tiger – and just as thrilling!\n"
                         "<b>- Tasks!</b> Roll up your sleeves and tackle intriguing mathematical challenges alongside me, as we exchange ideas and unravel the mysteries of numbers and patterns.",
                         reply_markup=InlineKeyboards().math_menu(),
                         parse_mode="HTML")

