"""
User Main Menu FSM Module.

This module defines a finite state machine (FSM) for handling the user's main menu state.

Classes:
    UserMainMenu: Defines states for the user's main menu.
"""

from aiogram.fsm.state import State, StatesGroup


class UserMainMenu(StatesGroup):
    menu = State()