from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from states.programming_state import ProgrammingState
import json
import random
from openai import OpenAI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from data.config import conf
from utils.db import db

programming_router = Router(name='programming')
programming_router.message.filter(ChatTypeFilter(chat_type=["private"]))

# programming menu
@programming_router.message(F.text == "Программирование")
async def programming_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="Выбери раздел:", reply_markup=InlineKeyboards().programming_menu())

# callback to return to the programming menu
@programming_router.callback_query(F.data == "programming_menu")
async def programming_menu_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выбери раздел:", reply_markup=InlineKeyboards().programming_menu())

# load tasks from JSON and pick random
def programming_tasks_get(level: str) -> dict:
    with open("assets/tasks_programming.json", "r") as file:
        tasks = json.load(file)
    return random.choice(tasks[level])

# check the answer for a task
def programming_tasks_check(task: dict, answer: str) -> bool:
    correct_answer = task["answer"]
    return answer.strip().lower() == correct_answer.lower()

# programmning menu tasks
@programming_router.callback_query(F.data == "programming_tasks")
async def programming_tasks_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Задачи.</b>\n\n"
                                     "Здесь тебя ждут разные задачи по советской информатике и программированию.", 
                                     reply_markup=InlineKeyboards().programming_tasks_start(), 
                                     parse_mode="HTML")


@programming_router.callback_query(F.data.in_({"programming_tasks_A", "programming_tasks_B", "programming_tasks_C"}))
async def programming_tasks_start_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    user_id = callback.from_user.id
    username = callback.from_user.username
    db.add_user(user_id, username)
    level = callback.data[-1] 
    task: dict = programming_tasks_get(level) 
    await callback.message.answer(task["question"])
    await state.set_state(ProgrammingState.answer)
    await state.update_data(task)


@programming_router.message(ProgrammingState.answer)
async def programming_tasks_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer: str = message.text
    task: dict = await state.get_data()
    result: bool = programming_tasks_check(task, answer)
    if result:
        await message.answer("Верно!", reply_markup=InlineKeyboards().programming_tasks_start_stop())
        db.add_score(message.from_user.id, 1)
    else:
        await message.answer("Неверно, попробуй ещё раз.", reply_markup=InlineKeyboards().programming_tasks_start_stop())


@programming_router.callback_query(F.data == "programming_tasks_table")
async def programming_tasks_table_handler(callback: types.CallbackQuery):
    users = db.get_users()
    table = "🏆 <b>Таблица рекордов:</b>\n\n"
    for user in users:
        table += f"👤 {user[1]} - {user[2]}\n"
    await callback.message.answer(table, parse_mode="HTML")

# callback to return to the programming menu after tasks
@programming_router.callback_query(ProgrammingState.answer, F.data == "programming_tasks_stop")
async def programming_tasks_stop_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Выбери раздел:", reply_markup=InlineKeyboards().programming_menu())
    await state.clear()

# translator
def programming_translator():
    # client = OpenAI(api_key=conf.openai_api_key)
    # response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "system", "content": "Ты - переводчик с современного языка программирования на советский."},
    #     {"role": "user", "content": "Who won the world series in 2020?"},
    #     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #     {"role": "user", "content": "Where was it played?"}
    # ]
    # )
    # return response.choices[0].message.content

    soviet_language = "REFAL"
    code = 'def main():\n\tprint("Hello world")'
    client = MistralClient(api_key=conf.mistral_api_key)
    messages = [
        ChatMessage(role="system", 
                    content="You're an experienced programmer with a vast knowledge of various programming languages and their syntaxes."
                    "You excel in translating code snippets from one language to another while retaining the original structure and style."
                    f"Your task is to translate a code snippet from a modern programming language to the Soviet programming language {soviet_language}." 
                    "The resulting code snippet should closely mimic the structure and style of the original code."
                    "Your response should only be in the form of code, without using any words."
                    f"Here is the code to translate: {code}"),
        ChatMessage(role="user", content=f'def main():\n\tprint("Hello world")'),
    ]
    chat_response = client.chat(model="mistral-large-latest", messages=messages)
    return chat_response.choices[0].message.content


@programming_router.callback_query(F.data == "programming_translator")
async def programming_translator_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    wait_message = await callback.message.answer("Пожалуйста, подождите...")
    await callback.message.answer(programming_translator())
    await wait_message.delete()
