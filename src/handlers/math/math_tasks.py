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

@math_tasks_router.callback_query(F.data == "math_tasks_table")
async def math_tasks_table_handler(callback: types.CallbackQuery):
    users = db.get_all_users()
    table = "🏆 <b>Leader board:</b>\n\n"
    for user in users:
        table += f"👤 {user[1]} - {user[2]}\n"
    await callback.message.answer(table, parse_mode="HTML")


# callback on tasks button from, math menu
@math_tasks_router.callback_query(F.data == "math_tasks")
async def math_handler_tasks(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Tasks", reply_markup=InlineKeyboards().math_tasks())


@math_tasks_router.callback_query(F.data == "math_tasks_start")
async def math_handler_tasks(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Choose difficulty:", reply_markup=InlineKeyboards().math_tasks_start())


# load tasks from JSON and pick random
def math_tasks_get(user_id: int, level: str) -> dict:
    with open("assets/json/tasks_math.json", "r") as file:
        tasks = json.load(file)
    unsolved_tasks = [i for i in tasks[level] if not db.task_exists(user_id, i["id"])]
    if unsolved_tasks:
        return random.choice(unsolved_tasks)
    else:
        return {"error": "All tasks are solved, stay tuned for more!"}
# check the answer for a task
    

def math_tasks_check(task: dict, answer: str) -> str:
    correct_answer = task["answer"]
    return answer.strip().lower() == correct_answer.lower()


@math_tasks_router.callback_query(F.data.in_({"math_tasks_A", "math_tasks_B", "math_tasks_C"}))
async def math_tasks_start_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    user_id = callback.from_user.id
    username = callback.from_user.username
    if not db.user_exists(user_id):
        db.add_user(user_id, username)
    level = callback.data[-1] 
    task: dict = math_tasks_get(user_id, level) 
    if "error" in task:
        await callback.message.answer(task["error"])
    else:
        global msg_photo
        global msg_text 
        task_id = task["id"]
        task_question = task["question"]
        task_photo = task["image"]
        msg_photo = await callback.message.answer_photo(FSInputFile(path=task_photo))
        msg_text = await callback.message.edit_text(f"<b>{task_id}.</b> {task_question}", parse_mode="HTML")
        await state.set_state(MathState.answer)
        await state.update_data(task)


@math_tasks_router.message(MathState.answer)
async def programming_tasks_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer: str = message.text
    task: dict = await state.get_data()
    result: bool = math_tasks_check(task, answer)
    if result:
        user_id = message.from_user.id
        task_id = task["id"][0]
        if task_id == "A":
            score = 1
        elif task_id == "B":
            score = 3
        elif task_id == "C":
            score = 3
        await msg_text.delete()
        await msg_photo.delete()
        await message.answer(f"<b>✅ Right!</b>\n\n+{score}!", reply_markup=InlineKeyboards().math_tasks_start_stop(), parse_mode="HTML")
        db.add_task(user_id, task["id"])
        db.add_score(user_id, score)
    else:
        await message.answer("❌ Wrong, try again.", reply_markup=InlineKeyboards().math_tasks_start_stop())


@math_tasks_router.message(MathState.answer)
async def programming_tasks_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer: str = message.text
    task: dict = await state.get_data()
    result: bool = math_tasks_check(task, answer)
    if result:
        await message.answer("Correct!", reply_markup=InlineKeyboards().math_tasks_start_stop())
        user_id = message.from_user.id
        db.add_task(user_id, task["id"])
        db.add_score(user_id, task["points"])
    else:
        await message.answer("Wrong, try again.", reply_markup=InlineKeyboards().math_tasks_start_stop())


@math_tasks_router.callback_query(F.data == "math_tasks_stop")
async def math_tasks_stop_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Choose section:", reply_markup=InlineKeyboards().math_tasks_start())
    await state.clear()
    
