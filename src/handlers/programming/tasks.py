from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.fsm.context import FSMContext
from states.programming_state import ProgrammingState
import json
import random
from utils.db import db

programming_tasks_router = Router(name='programming_tasks')
programming_tasks_router.message.filter(ChatTypeFilter(chat_type=["private"]))

# load tasks from JSON and pick random
def programming_tasks_get(user_id: int, level: str) -> dict:
    with open("assets/json/tasks_programming.json", "r") as file:
        tasks = json.load(file)
    unsolved_tasks = [i for i in tasks[level] if not db.task_exists(user_id, i["id"])]
    if unsolved_tasks:
        return random.choice(unsolved_tasks)
    else:
        return {"error": f"All tasks are solved, stay tuned for more!"}

# check the answer xfor a task
def programming_tasks_check(task: dict, answer: str) -> bool:
    correct_answer = task["answer"]
    return answer.strip().lower() == correct_answer.lower()

# programmning menu tasks
@programming_tasks_router.callback_query(F.data == "programming_tasks")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Tasks.</b>\n\n"
                                     "Here you can solve different soviet programming tasks.", 
                                     reply_markup=InlineKeyboards().programming_tasks_start(), 
                                     parse_mode="HTML")


@programming_tasks_router.callback_query(F.data.in_({"programming_tasks_A", "programming_tasks_B", "programming_tasks_C"}))
async def programming_tasks_start_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    user_id = callback.from_user.id
    username = callback.from_user.username
    if not db.user_exists(user_id):
        db.add_user(user_id, username)
    level = callback.data[-1] 
    task: dict = programming_tasks_get(user_id, level) 
    if "error" in task:
        await callback.message.edit_text(task["error"], reply_markup=InlineKeyboards().programming_tasks_back())
    else:
        await callback.message.edit_text(f"<b>{task["id"]}.</b> {task["question"]}", parse_mode="HTML")
        await state.set_state(ProgrammingState.answer)
        await state.update_data(task)


@programming_tasks_router.message(ProgrammingState.answer)
async def programming_tasks_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer: str = message.text
    task: dict = await state.get_data()
    result: bool = programming_tasks_check(task, answer)
    if result:
        user_id = message.from_user.id
        task_id = task["id"][0]
        if task_id == "A":
            score = 1
        elif task_id == "B":
            score = 3
        elif task_id == "C":
            score = 5
        await message.answer(f"<b>✅ Right!</b>\n\n+{score}!", reply_markup=InlineKeyboards().programming_tasks_start_stop(), parse_mode="HTML")
        db.add_task(user_id, task["id"])
        db.add_score(user_id, score)
    else:
        await message.answer("❌ Wrong, try again.", reply_markup=InlineKeyboards().programming_tasks_start_stop())


@programming_tasks_router.callback_query(F.data == "programming_tasks_table")
async def programming_tasks_table_handler(callback: types.CallbackQuery):
    users = db.get_all_users()
    table = "🏆 <b>Records:</b>\n\n"
    for user in users:
        table += f"👤 @{user[1]} - {user[2]}\n"
    await callback.message.edit_text(table, reply_markup=InlineKeyboards().programming_tasks_back(), parse_mode="HTML")

# callback to return to the programming menu after tasks
@programming_tasks_router.callback_query(ProgrammingState.answer, F.data == "programming_tasks_stop")
async def programming_tasks_stop_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Choose a section:", reply_markup=InlineKeyboards().programming_menu())
    await state.clear()
