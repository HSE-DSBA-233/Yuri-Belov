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

    
    def history_math(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="The Beginnings", callback_data="history_math_beginnings")
            ],
            [
                self.button(text="Moscow State University", callback_data="history_math_msu")
            ],
            [
                self.button(text="USSR", callback_data="history_math_ussr")
            ],
            [
                self.button(text="Lev Pontryagin", callback_data="history_math_pontryagin")
            ],
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)    
    

    def history_programming(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Part 1", callback_data="history_programming_part1")
            ],
            [
                self.button(text="Part 2", callback_data="history_prorgamming_part2")
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)    
    

    def history_programming(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Part 1", callback_data="history_programming_part1")
            ],
            [
                self.button(text="Part 2", callback_data="history_programming_part2")
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)    