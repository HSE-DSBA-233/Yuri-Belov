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
                self.button(text="History", callback_data="history_programming"),
                self.button(text="Theory", callback_data="programming_theory"),
                self.button(text="Tasks", callback_data="programming_tasks")
            ],
            [
                self.button(text="Translator", callback_data="programming_translator")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def programming_tasks_start(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Easy", callback_data="programming_tasks_A"),
                self.button(text="Medium", callback_data="programming_tasks_B"),
                self.button(text="Hard", callback_data="programming_tasks_C")

            ],
            [
                self.button(text="Records", callback_data="programming_tasks_table")
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)


    def programming_tasks_start_stop(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Easy", callback_data="programming_tasks_A"),
                self.button(text="Medium", callback_data="programming_tasks_B"),
                self.button(text="Hard", callback_data="programming_tasks_C")

            ],
            [
                self.button(text="I don't want to solve anymore", callback_data="programming_tasks_stop")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def programming_tasks_back(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="programming_tasks")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
