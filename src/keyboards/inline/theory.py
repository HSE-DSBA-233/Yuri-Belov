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
                self.button(text="RAPIRA", callback_data="theory_rapira")
            ],
            [
                self.button(text="El-76", callback_data="theory_el76"),
            ],
            [
                self.button(text="⬅️", callback_data="programming_menu")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    
    # refal-5 theory begins here
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
    
    # el-76 theory begins here
    def back_to_theory_el76(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="theory_el76")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    
    def theory_el76(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="History", callback_data="el76_history"),
            ],
            [
                self.button(text="Syntax overview", callback_data="el76_syntax"),
            ],
            [
                self.button(text="Basic operations", callback_data="el76_operators"),
            ],
            [
                self.button(text="Code examples", callback_data="el76_examples"),
            ],
            [
                self.button(text="⬅️", callback_data="programming_theory")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    # rapira theory begins here
    def theory_rapira(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Objects and operations", callback_data="rapira_objects"),
            ],
            [
                self.button(text="Sequences", callback_data="rapira_sequences"),
            ],
            [
                self.button(text="Variables", callback_data="rapira_variables"),
            ],
            [
                self.button(text="Slices and selections", callback_data="rapira_slices"),
            ],
            [
                self.button(text="Statements", callback_data="rapira_statements"),
            ],
            [
                self.button(text="Modules and devices", callback_data="rapira_modules"),
            ],
            [
                self.button(text="Russian equivalents of functions", callback_data="rapira_equivalents"),
            ],
            [
                self.button(text="Other examples", callback_data="rapira_others"),
            ],
            [
                self.button(text="⬅️", callback_data="programming_theory")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    
    def back_to_theory_rapira(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="theory_rapira")
            ],
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def back_to_theory_rapira_statements(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="Proceed to hypothetical game", callback_data="rapira_statements_game")
            ],
            [
                self.button(text="⬅️", callback_data="theory_rapira")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)
    

    def back_to_theory_rapira_statements_game(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                self.button(text="⬅️", callback_data="rapira_statements")
            ]
        ]
        return self.keyboard(inline_keyboard=buttons)