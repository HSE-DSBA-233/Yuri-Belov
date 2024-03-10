from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class InlineKeyboards:
    def __init__(self) -> None:
        self.keyboard = InlineKeyboardMarkup
        self.button = InlineKeyboardButton


    def programming_theory(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="REFAL-5", callback_data="theory_refal"),
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def theory_refal(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Basic syntax and construct", callback_data="refal_intro"),
            ],
            [
                self.button(text="Basic operations", callback_data="refal_operators"),
            ],
            [
                self.button(text="Lists", callback_data="refal_lists"),
            ],
            [
                self.button(text="Patterns", callback_data="refal_patterns"),
            ],
            [
                self.button(text="Recursion", callback_data="refal_recursion"),
            ],
            [
                self.button(text="⬅️", callback_data="programming_theory")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def back_to_theory_refal(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="theory_refal")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    