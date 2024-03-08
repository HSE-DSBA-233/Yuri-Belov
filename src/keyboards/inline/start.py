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
                self.button(text="History", callback_data="history"),
                self.button(text="Math", callback_data="math"),
                self.button(text="Programming", callback_data="programming")
            ],
            [
                self.button(text="start", callback_data="start")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)

