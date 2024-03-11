from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter

programming_router = Router(name='programming')
programming_router.message.filter(ChatTypeFilter(chat_type=["private"]))

# programming menu
@programming_router.message(F.text == "Programming")
async def programming_handler(message: types.Message):
    handler(__name__, type=message)
    await message.answer(text="Choose a section:", reply_markup=InlineKeyboards().programming_menu())

# callback to return to the programming menu
@programming_router.callback_query(F.data == "programming_menu")
async def programming_menu_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Choose a section:", reply_markup=InlineKeyboards().programming_menu())
