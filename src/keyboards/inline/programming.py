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
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def programming_tasks_start(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Начать решать задачи", callback_data="programming_tasks_start")
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)


    def programming_tasks_start_stop(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Продолжить", callback_data="programming_tasks_start")
            ],
            [
                self.button(text="Я больше не хочу решать", callback_data="programming_tasks_stop")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
