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


math_tasks_router = Router(name='math_tasks')
math_tasks_router.message.filter(ChatTypeFilter(chat_type=["private"]))


"""
LOGIC SECTION FOR TASKS
"""


# callback on tasks button from, math menu
@math_tasks_router.callback_query(F.data == "math_tasks")
async def math_handler_tasks(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Задачи", reply_markup=InlineKeyboards().math_tasks())


@math_tasks_router.callback_query(F.data == "math_tasks_start")
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


@math_tasks_router.callback_query(F.data == "math_tasks_table")
async def math_tasks_table_handler(callback: types.CallbackQuery):
    users = db.get_users()
    table = "🏆 <b>Таблица рекордов:</b>\n\n"
    for user in users:
        table += f"👤 {user[1]} - {user[2]}\n"
    await callback.message.answer(table, parse_mode="HTML")


#Easy
@math_tasks_router.callback_query(F.data == "math_tasks_easy")
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
@math_tasks_router.callback_query(F.data == "math_tasks_medium")
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
@math_tasks_router.callback_query(F.data == "math_tasks_hard")
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
@math_tasks_router.message(MathState.answer_math_easy)
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
@math_tasks_router.message(MathState.answer_math_medium)
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
@math_tasks_router.message(MathState.answer_math_hard)
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


@math_tasks_router.callback_query(F.data == "math_tasks_stop")
async def math_tasks_stop_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выбери раздел:", reply_markup=InlineKeyboards().math_tasks_start())
    await state.clear()
    