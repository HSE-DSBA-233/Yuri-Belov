from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from utils.logging import handler
from keyboards.inline.math import InlineKeyboards
from filters.chat_type import ChatTypeFilter

math_router = Router(name='math')
math_router.message.filter(ChatTypeFilter(chat_type=["private"]))


# default keyboard
@math_router.message(F.text == "Математика")
async def math_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer("Выберите раздел:", reply_markup=InlineKeyboards().math_menu())


# callback on math
@math_router.callback_query(F.data == "math")
async def programming_theory_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Выберите раздел:", reply_markup=InlineKeyboards().math_menu())


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


# callback on history button from math menu
@math_router.callback_query(F.data == "math_history")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="История", reply_markup=InlineKeyboards().math_history())


# callback on soviet math
@math_router.callback_query(F.data == "math_introduction")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
            f"<b>Отличие советской математики от мировой</b>\n\n"
            f"<b>Формализм и строгость:</b>\n"
            f"Советская математическая школа акцентировала внимание на строгом и формальном подходе к математике. Учащиеся изучали математику с акцентом на доказательства и теоретическое понимание, в отличие от более прикладного или практического подхода, который мог быть распространен в других странах.\n\n"
            f"<b>Внимание к основам:</b>\n" 
            f"Особое внимание в советской системе образования уделялось закладыванию прочных основ математических знаний у учащихся. Была разработана специальная методика для формирования у школьников умений абстрактного мышления и логического анализа.\n\n"
            f"<b>Интеграция с физикой и другими науками:</b>\n" 
            f"В советских школах и вузах был распространен междисциплинарный подход, в рамках которого математика тесно переплеталась с физикой и другими точными науками. Это создавало более глубокое понимание связей между различными областями знаний.\n\n"
            f"<b>Соревновательный дух:</b>\n" 
            f"В СССР была развита система математических олимпиад и соревнований, которые способствовали росту интереса к математике среди школьников и студентов. Эти соревнования также служили платформой для выявления и поддержки одаренных учащихся.\n"
            ), 
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboards().math_introduction()
        )


# callback on history button from math menu
@math_router.callback_query(F.data == "math_books_lobby")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выберите раздел математики:", reply_markup=InlineKeyboards().math_books_lobby())
