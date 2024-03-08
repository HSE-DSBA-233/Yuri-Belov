"""
Inline Keyboards Module.

This module provides a class for generating inline keyboards with various buttons.

Classes:
    InlineKeyboards: Generates inline keyboards with predefined buttons.
"""

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineKeyboards:
    def __init__(self) -> None:
        self.keyboard = InlineKeyboardMarkup
        self.button = InlineKeyboardButton


    def start(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Математика", callback_data="math_menu"),
                self.button(text="Программирование", callback_data="programming")
            ],
            [
                self.button(text="О боте", callback_data="about")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)

    def start_about(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="start")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)

