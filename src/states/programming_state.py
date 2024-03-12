from aiogram.fsm.state import State, StatesGroup


class ProgrammingTasksState(StatesGroup):
    answer = State()


class ProgrammingTranslatorState(StatesGroup):
    code = State()
