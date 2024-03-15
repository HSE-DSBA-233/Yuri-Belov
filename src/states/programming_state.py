from aiogram.fsm.state import State, StatesGroup


class ProgrammingTasksState(StatesGroup):
    A = State()
    B_and_C = State()


class ProgrammingTranslatorState(StatesGroup):
    code = State()
