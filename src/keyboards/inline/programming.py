"""
Inline Keyboards Module.

This module provides a class for generating inline keyboards with various buttons.

Classes:
    InlineKeyboards: Generates inline keyboards with predefined buttons.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineKeyboards:
    def __init__(self) -> None:
        self.keyboard = InlineKeyboardMarkup
        self.button = InlineKeyboardButton


    def programming_menu(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="История", callback_data="programming_history"),
                self.button(text="Теория", callback_data="programming_theory"),
                self.button(text="Задачи", callback_data="programming_tasks")
            ],
            [
                self.button(text="Переводчик", callback_data="programming_translator")
            ],
            [
                self.button(text="⬅️", callback_data="start")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
