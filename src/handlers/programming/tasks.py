from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.fsm.context import FSMContext
from states.programming_state import ProgrammingTasksState
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
        return {"error": "Congratulations, dear comrade! You've successfully solved all the current tasks. Keep your eyes peeled for more intriguing challenges, as I'm constantly working on expanding our collection. Stay tuned, and let's continue this thrilling journey through the world of Soviet programming together!"}


# check the answer xfor a task
def programming_tasks_check(task: dict, answer: str) -> bool:
    correct_answer = task["answer"]
    return answer.strip().lower() == correct_answer.lower()


# programmning menu tasks
@programming_tasks_router.callback_query(F.data == "programming_tasks")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Tasks!</b>\n\n"
                                     "Here, I'll share with you delightful programming tasks from the Soviet era. After solving them, you might even find yourself on the leaderboard! What are you waiting for? The tea's getting cold, swiftly choose your difficulty level:", 
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
        task_id = task["id"]
        task_question = task["question"]
        await callback.message.edit_text(f"<b>{task_id}.</b> {task_question}", parse_mode="HTML")
        await state.set_state(ProgrammingTasksState.answer)
        await state.update_data(task)


@programming_tasks_router.message(ProgrammingTasksState.answer)
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
        await message.answer(f"<b>Absolutely correct, comrade!</b>\n\n<b>+{score} points!</b> Keep up the fantastic work, and let's continue to explore the captivating world of Soviet programming together!", reply_markup=InlineKeyboards().programming_tasks_start_stop(), parse_mode="HTML")
        db.add_task(user_id, task["id"])
        db.add_score(user_id, score)
    else:
        await message.answer("Not quite right, my friend, give it another go!", reply_markup=InlineKeyboards().programming_tasks_start_stop())


@programming_tasks_router.callback_query(F.data == "programming_tasks_table")
async def programming_tasks_table_handler(callback: types.CallbackQuery):
    users = db.get_all_users()
    table = "<b>My cherished leaderboard of brilliant programmers:</b>\n\n"
    for user in users:
        table += f"👤 @{user[1]} - {user[2]}\n"
    await callback.message.edit_text(table, reply_markup=InlineKeyboards().programming_tasks_back(), parse_mode="HTML")


# callback to return to the programming menu after tasks
@programming_tasks_router.callback_query(ProgrammingTasksState.answer, F.data == "programming_tasks_stop")
async def programming_tasks_stop_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Programming:</b>\n\n"
                         "This is the programming section, my dear comrade! A splendid sanctuary where the marvels of technology come to life, guided by the wisdom of my Soviet heritage. "
                         "Just for you, I've crafted these enchanting buttons below to guide our conversation, choose your desired destination swiftly:\n\n"
                         "<b>- History!</b> Join me in celebrating the glorious past of programming, as we pay homage to the pioneering achievements of our fellow Soviets.\n"
                         "<b>- Theory!</b> Let's delve into the fascinating concepts of Soviet programming languages, as I share my insights from years in the field.\n"
                         "<b>- Tasks!</b> Roll up your sleeves and tackle programming challenges alongside me, as we exchange ideas and unravel the mysteries of algorithms and solutions.\n"
                         "<b>- Code Translator!</b> Together, we'll bridge the gap between past and present by translating modern programming languages into their Soviet-era equivalents.", 
                         reply_markup=InlineKeyboards().programming_menu(), 
                         parse_mode="HTML")
    await state.clear()
