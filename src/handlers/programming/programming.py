from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.fsm.context import FSMContext

programming_router = Router(name='programming')
programming_router.message.filter(ChatTypeFilter(chat_type=["private"]))


# programming menu
@programming_router.message(F.text == "Programming")
async def programming_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    await state.clear()
    await message.answer("<b>Programming:</b>\n\n"
                         "This is the programming section, my dear comrade! A splendid sanctuary where the marvels of technology come to life, guided by the wisdom of my Soviet heritage. "
                         "Just for you, I've crafted these enchanting buttons below to guide our conversation, choose your desired destination swiftly:\n\n"
                         "<b>- History!</b> Join me in celebrating the glorious past of programming, as we pay homage to the pioneering achievements of our fellow Soviets.\n"
                         "<b>- Theory!</b> Let's delve into the fascinating concepts of Soviet programming languages, as I share my insights from years in the field.\n"
                         "<b>- Tasks!</b> Roll up your sleeves and tackle programming challenges alongside me, as we exchange ideas and unravel the mysteries of algorithms and solutions.\n"
                         "<b>- Code Translator!</b> Together, we'll bridge the gap between past and present by translating modern programming languages into their Soviet-era equivalents.", 
                         reply_markup=InlineKeyboards().programming_menu(), 
                         parse_mode="HTML")


# callback to return to the programming menu
@programming_router.callback_query(F.data == "programming_menu")
async def programming_menu_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Programming:</b>\n\n"
                         "This is the programming section, my dear comrade! A splendid sanctuary where the marvels of technology come to life, guided by the wisdom of my Soviet heritage. "
                         "Just for you, I've crafted these enchanting buttons below to guide our conversation, choose your desired destination swiftly:\n\n"
                         "<b>- History!</b> Join me in celebrating the glorious past of programming, as we pay homage to the pioneering achievements of our fellow Soviets.\n"
                         "<b>- Theory!</b> Let's delve into the fascinating concepts of Soviet programming languages, as I share my insights from years in the field.\n"
                         "<b>- Tasks!</b> Roll up your sleeves and tackle programming challenges alongside me, as we exchange ideas and unravel the mysteries of algorithms and solutions.\n"
                         "<b>- Code Translator!</b> Together, we'll bridge the gap between past and present by translating modern programming languages into their Soviet-era equivalents.", 
                         reply_markup=InlineKeyboards().programming_menu(), 
                         parse_mode="HTML")
