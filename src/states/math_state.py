from aiogram.fsm.state import State, StatesGroup


class MathState(StatesGroup):
    question = State()
    answer = State()
    answer_math_easy = State()
    answer_math_medium = State()
    answer_math_hard = State()
