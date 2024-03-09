from aiogram.fsm.state import State, StatesGroup


class ProgrammingState(StatesGroup):
    question = State()
    answer = State()
