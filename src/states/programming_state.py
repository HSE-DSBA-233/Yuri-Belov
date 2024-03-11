from aiogram.fsm.state import State, StatesGroup


class ProgrammingState(StatesGroup):
    answer = State()
