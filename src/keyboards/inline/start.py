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
                self.button(text="start", callback_data="start")
            ],
            [
                self.button(text="start", callback_data="start")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
