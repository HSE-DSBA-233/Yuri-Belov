from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from states.programming_state import ProgrammingState
import json
import random

programming_router = Router(name='programming')
programming_router.message.filter(ChatTypeFilter(chat_type=["private"]))


@programming_router.message(F.text == "Программирование")
async def programming_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="Выбери раздел:", reply_markup=InlineKeyboards().programming_menu())


@programming_router.callback_query(F.data == "programming_theory")
async def programming_theory_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Теория")

# Load tasks from JSON and pick random
def programming_tasks_get() -> dict:
    with open("assets/tasks_programming.json", "r") as file:
        tasks = json.load(file)
    return random.choice(tasks)

# Check the answer for a task
def programming_tasks_check(task: dict, answer: str) -> str:
    correct_answer = task["answer"]
    if answer.strip().lower() == correct_answer.lower():
        return "Верно"
    else:
        return "Неверно, осталось попытки: "


@programming_router.callback_query(F.data == "programming_tasks")
async def programming_tasks_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    task: dict = programming_tasks_get() 
    await callback.message.answer(task["question"])
    await state.set_state(ProgrammingState.answer)
    await state.update_data(task)


@programming_router.message(ProgrammingState.answer)
async def programming_tasks_check_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    answer = message.text
    task: dict = await state.get_data()
    await message.answer(programming_tasks_check(task, answer))
    await state.clear()


@programming_router.callback_query(F.data == "programming_translator")
async def programming_translator_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Переводчик")
