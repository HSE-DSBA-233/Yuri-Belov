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
                self.button(text="The Mathematical-Navigational School", callback_data="history_math_school")
            ],
            [
                self.button(text="Moscow State University", callback_data="history_math_msu")
            ],
            [
                self.button(text="The 20th Century and Beyond", callback_data="history_math_20th")
            ],
            [
                self.button(text="⬅️", callback_data="math")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)    
    

    def history_programming(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="The Beginnings", callback_data="history_math_beginning")
            ],
            [
                self.button(text="The Mathematical-Navigational School", callback_data="history_math_school")
            ],
            [
                self.button(text="Moscow State University", callback_data="history_math_msu")
            ],
            [
                self.button(text="The 20th Century and Beyond", callback_data="history_math_20th")
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)    