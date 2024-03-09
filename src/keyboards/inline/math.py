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
                self.button(text="Что такое советская математика", callback_data="math_introduction"),
            ],
            [
                self.button(text="Разделы математики", callback_data="math_books_lobby")
            ],
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)


# Keyboards with differences between soviet and world wide math
    def math_introduction(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="math_theory")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)


# Books
    def math_books_lobby(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Математический анализ", callback_data="math_introduction"),
                self.button(text="Алгебра", callback_data="math_introduction"),
            ],
            [
                self.button(text="Геометрия и топология", callback_data="math_introduction"),
                self.button(text="Дифференциальные уравнения", callback_data="math_introduction"),
            ],
            [
                self.button(text="Теория функций", callback_data="math_introduction"),
                self.button(text="Функциональный анализ", callback_data="math_introduction"),
            ],
            [
                self.button(text="Теория вероятностей и математическая статистика", callback_data="math_introduction"),
                self.button(text="Численные методы", callback_data="math_introduction"),
            ],
            [
                self.button(text="Дискретная математика", callback_data="math_introduction"),
                self.button(text="Математическая логика и теория множеств", callback_data="math_introduction"),
            ],
            [
                self.button(text="Дифференциальная геометрия", callback_data="math_introduction"),
                self.button(text="Теория чисел", callback_data="math_introduction"),
            ],
            [
                self.button(text="Оптимизация и вариационное исчисление", callback_data="math_introduction"),
                self.button(text="Теория управления и оптимизации", callback_data="math_introduction"),
            ],
            [
                self.button(text="Математическая физика", callback_data="math_introduction"),
            ],
            [
                self.button(text="⬅️", callback_data="math_theory")
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
