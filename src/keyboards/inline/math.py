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
                self.button(text="History", callback_data="history_math"),
                self.button(text="Theory", callback_data="math_theory"),
                self.button(text="Tasks", callback_data="math_tasks")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

# Keyboard with theory menu
    def math_theory(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Specifics of Soviet mathematics", callback_data="math_introduction"),
            ],
            [
                self.button(text="Areas of mathematics", callback_data="math_books_lobby")
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
                self.button(text="Математический анализ", callback_data="math_book_analysis"),
                self.button(text="Алгебра", callback_data="math_book_algebra"),
            ],
            [
                self.button(text="Геометрия и топология", callback_data="math_book_geometry"),
                self.button(text="Дифференциальные уравнения", callback_data="math_book_differential"),
            ],
            [
                self.button(text="Теория функций", callback_data="math_functions"),
                self.button(text="Функциональный анализ", callback_data="math_book_functionsAnalysis"),
            ],
            [
                self.button(text="Теория вероятностей и математическая статистика", callback_data="math_book_probability"),
                self.button(text="Численные методы", callback_data="math_book_numberMethods"),
            ],
            [
                self.button(text="Дискретная математика", callback_data="math_book_discrete"),
                self.button(text="Математическая логика и теория множеств", callback_data="math_book_logic"),
            ],
            [
                self.button(text="Дифференциальная геометрия", callback_data="math_book_diffGeometry"),
                self.button(text="Теория чисел", callback_data="math_numberTheory"),
            ],
            [
                self.button(text="Оптимизация и вариационное исчисление", callback_data="math_book_optimization"),
                self.button(text="Теория управления и оптимизации", callback_data="math_book_managment"),
            ],
            [
                self.button(text="Математическая физика", callback_data="math_book_physics"),
            ],
            [
                self.button(text="⬅️", callback_data="math_theory")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    


# Keyboard with task page
    def math_tasks_start(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="High school level", callback_data="math_tasks_A"),
                self.button(text="University level", callback_data="math_tasks_B"),
                self.button(text="School olympiad level", callback_data="math_tasks_C")
            ],
            [
                self.button(text="⬅️", callback_data="math_tasks")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def math_tasks(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Start solving problems", callback_data="math_tasks_start")
            ],
            [
                self.button(text="Leader board", callback_data="math_tasks_table")
            ],
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)


    def math_tasks_start_stop(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="High school level", callback_data="math_tasks_A"),
                self.button(text="University level", callback_data="math_tasks_B"),
                self.button(text="School olympiad level", callback_data="math_tasks_C")
            ],
            [
                self.button(text="I don't want to solve anymore", callback_data="math_tasks_stop")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    