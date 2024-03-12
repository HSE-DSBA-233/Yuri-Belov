from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class DefaultKeyboards:
    def __init__(self) -> None:
        self.keyboard = ReplyKeyboardMarkup
        self.button = KeyboardButton


    def start_default_keyboard(self) -> ReplyKeyboardMarkup:
        buttons = [
            [
                self.button(text="Математика"),
                self.button(text="Programming")
            ],
            [
                self.button(text="About")
            ]
        ]
        return self.keyboard(keyboard=buttons, resize_keyboard=True)
