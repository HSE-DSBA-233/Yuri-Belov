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


# Keyboard with math start menu
    def math_menu(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="История", callback_data="math_history"),
                self.button(text="Теория", callback_data="math_theory"),
                self.button(text="Задачи", callback_data="math_tasks")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

# Keyboard with history menu
    def math_history(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

# Keyboard with theory menu
    def math_theory(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Что такое математика", callback_data="math_introduction"),
                self.button(text="Что такое советская математика", callback_data="math_introduction_soviet"),
            ],
            [
                self.button(text="Разделы математики", callback_data="math_books_lobby")
            ],
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)


# Keyboard with task page
    def math_tasks(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Простой уровень", callback_data="math_tasks_easy"),
                self.button(text="Средний уровень", callback_data="math_tasks_medium"),
                self.button(text="Продвинутый уровень", callback_data="math_tasks_advanced")
            ],
            [
                self.button(text="Уровень Советского пятикласника", callback_data="math_tasks_olympiad"),
            ],
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
