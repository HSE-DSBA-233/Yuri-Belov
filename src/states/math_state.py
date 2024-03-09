from aiogram.fsm.state import State, StatesGroup


class MathState(StatesGroup):
    question = State()
    answer = State()
