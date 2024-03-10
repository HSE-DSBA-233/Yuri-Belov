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


# default keyboard
@math_router.message(F.text == "Математика")
async def math_handler_menu(message: types.Message):
    handler(__name__, type=message)
    await message.answer("Выберите раздел:", reply_markup=InlineKeyboards().math_menu())


# callback on math
@math_router.callback_query(F.data == "math")
async def math_handler_menu(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Выберите раздел:", reply_markup=InlineKeyboards().math_menu())


# callback on theory button from, math menu
@math_router.callback_query(F.data == "math_theory")
async def math_handler_theory(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Теория", reply_markup=InlineKeyboards().math_theory())


"""
BOOKS SECTION
"""

#Fixtengolz
@math_router.callback_query(F.data == "math_book_analysis")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/1968Fixtengolz1-2_compressed.pdf"), caption="Математический анализ, Фихтенгольц")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_algebra")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/Kostrikin_A_I_-_Vvedenie_v_algebru_Chast_I_Osnovy_algebry_2000_FIZMATLIT_compressed.pdf"), caption="Введение в алгебру, Костринкин")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_geometry")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/TopologyAndGeometry.pdf"), caption="Основы общей топологии в задачах и упражнениях Архангельский, Пономарев")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_differential")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/differentialPt1.pdf"), caption="ЛЕКЦИИ ПО ОБЫКНОВЕННЫМ ДИФФЕРЕНЦИАЛЬНЫМ УРАВНЕНИЯМ Ч.1 Мамонтов")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/differentialPt2.pdf"), caption="ЛЕКЦИИ ПО ОБЫКНОВЕННЫМ ДИФФЕРЕНЦИАЛЬНЫМ УРАВНЕНИЯМ Ч.2 Мамонтов")
    await msg.delete()


@math_router.callback_query(F.data == "math_functions")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/Volkovyskiy_L_I__Lunts_G_L__Aramanovich_I_G_-_Sbornik_zadach_po_teorii_funktsiy_komplexnogo_peremennogo_-_2004_compressed.pdf"), caption="Задачник Волковыский по теории функций комплексного переменного")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_functionsAnalysis")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/FunctionalAnalysis.pdf"), caption="Функциональный анализ, Канторович")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_probability")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/ProbTheory_compressed.pdf"), caption="Курс теории вероятностей, Гнеденко")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_numberMethods")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/Samarskiy_1989_432_compressed.pdf"), caption="Численные методы, Самарский")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_discrete")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/discra_compressed.pdf"), caption="Дискретная математика для программистов, Новиков")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_logic")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/MATLOGIC.pdf"), caption="Математическая логика, Ершов, Полютин")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_diffGeometry")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/diffGeomp1.pdf"), caption="Лекции по диффференциальной геометрии Ч1, Тайманов")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/diffGeomp2.pdf"), caption="Лекции по диффференциальной геометрии Ч2, Тайманов")
    await msg.delete()


@math_router.callback_query(F.data == "math_numberTheory")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/osnovy_teorii_chisel.pdf"), caption="Основы теории чисел, Винградов")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_optimization")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/Elsgolc1969ru_compressed.pdf"), caption="Дифферинциальные уравнения и Вариационное исчисление, Эльсгольц")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_managment")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/Managment.pdf"), caption="Проблемы управления")
    await msg.delete()


@math_router.callback_query(F.data == "math_book_physics")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("Отправка книги, пожалуйста подождите...")
    await callback.message.reply_document(FSInputFile(path="assets/mathBooks/vladimirov-lectures-1981_compressed.pdf"), caption="Уравнение математический физики, Владимиров")
    await msg.delete()
"""
BOOKS SECTION
"""


# callback on soviet math
@math_router.callback_query(F.data == "math_introduction")
async def math_handler_theory_introduction(callback: types.CallbackQuery):
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
async def math_handler_books(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выберите раздел математики:", reply_markup=InlineKeyboards().math_books_lobby())


"""
LOGIC SECTION FOR TASKS
"""


# callback on tasks button from, math menu
@math_router.callback_query(F.data == "math_tasks")
async def math_handler_tasks(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Задачи", reply_markup=InlineKeyboards().math_tasks())


@math_router.callback_query(F.data == "math_tasks_start")
async def math_handler_tasks(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выберите уровень сложности:", reply_markup=InlineKeyboards().math_tasks_start())


# load tasks from JSON and pick random
def math_easy_tasks_get() -> dict:
    with open("assets/tasks_math_easy.json", "r") as file:
        tasks = json.load(file)
    return random.choice(tasks)


def math_medium_tasks_get() -> dict:
    with open("assets/tasks_math_medium.json", "r") as file:
        tasks = json.load(file)
    return random.choice(tasks)


def math_hard_tasks_get() -> dict:
    with open("assets/tasks_math_hard.json", "r") as file:
        tasks = json.load(file)
    return random.choice(tasks)

# check the answer for a task
def math_tasks_check(task: dict, answer: str) -> str:
    correct_answer = task["answer"]
    if answer.strip().lower() == correct_answer.lower():
        return True
    else:
        return False


@math_router.callback_query(F.data == "math_tasks_table")
async def math_tasks_table_handler(callback: types.CallbackQuery):
    users = db.get_users()
    table = "🏆 <b>Таблица рекордов:</b>\n\n"
    for user in users:
        table += f"👤 {user[1]} - {user[2]}\n"
    await callback.message.answer(table, parse_mode="HTML")


#Easy
@math_router.callback_query(F.data == "math_tasks_easy")
async def math_tasks_easy_start_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    user_id = callback.from_user.id
    username = callback.from_user.username
    if not db.user_exists(user_id):
        db.add_user(user_id, username)
    task: dict = math_easy_tasks_get() 
    await callback.message.answer(task["question"])
    await state.set_state(MathState.answer_math_easy)
    await state.update_data(task)


#Medium
@math_router.callback_query(F.data == "math_tasks_medium")
async def math_tasks_medium_start_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    user_id = callback.from_user.id
    username = callback.from_user.username
    if not db.user_exists(user_id):
        db.add_user(user_id, username)
    task: dict = math_medium_tasks_get() 
    await callback.message.answer(task["question"])
    await state.set_state(MathState.answer_math_medium)
    await state.update_data(task)    


#Hard
@math_router.callback_query(F.data == "math_tasks_hard")
async def math_tasks_hard_start_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    user_id = callback.from_user.id
    username = callback.from_user.username
    if not db.user_exists(user_id):
        db.add_user(user_id, username)
    task: dict = math_hard_tasks_get() 
    await callback.message.answer(task["question"])
    await state.set_state(MathState.answer_math_hard)
    await state.update_data(task)


#Easy
@math_router.message(MathState.answer_math_easy)
async def math_tasks_easy_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer = message.text
    task: dict = await state.get_data()
    result: bool = math_tasks_check(task, answer)
    if result:
        await message.answer("Верно!", reply_markup=InlineKeyboards().math_tasks_easy())
        db.add_score(message.from_user.id, 1)
    else:
        await message.answer("Неверно, попробуй ещё раз.", reply_markup=InlineKeyboards().math_tasks_easy())


#Medium
@math_router.message(MathState.answer_math_medium)
async def math_tasks_easy_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer = message.text
    task: dict = await state.get_data()
    result: bool = math_tasks_check(task, answer)
    if result:
        await message.answer("Верно!", reply_markup=InlineKeyboards().math_tasks_medium())
        db.add_score(message.from_user.id, 5)
    else:
        await message.answer("Неверно, попробуй ещё раз.", reply_markup=InlineKeyboards().math_tasks_medium())


#Hard
@math_router.message(MathState.answer_math_hard)
async def math_tasks_easy_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer = message.text
    task: dict = await state.get_data()
    result: bool = math_tasks_check(task, answer)
    if result:
        await message.answer("Верно!", reply_markup=InlineKeyboards().math_tasks_hard())
        db.add_score(message.from_user.id, 10)
    else:
        await message.answer("Неверно, попробуй ещё раз.", reply_markup=InlineKeyboards().math_tasks_hard())


@math_router.callback_query(F.data == "math_tasks_stop")
async def math_tasks_stop_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выбери раздел:", reply_markup=InlineKeyboards().math_tasks_start())
    await state.clear()
    