from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from utils.logging import handler
from keyboards.inline.history import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.types import FSInputFile

history_router = Router(name='history')
history_router.message.filter(ChatTypeFilter(chat_type=["private"]))


# callback on history button from math menu
@history_router.callback_query(F.data == "history_math")
async def history_math_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>History!</b>\n\n"
                                     "My dear comrade, we have now dived into the rich tapestry of Soviet mathematical history! Prepare to be enthralled by tales of brilliant minds! Let's uncover the stories that have defined the Soviet mathematical legacy!", 
                                     reply_markup=InlineKeyboards().history_math(),
                                     parse_mode="HTML")


@history_router.callback_query(F.data == "history_math_beginnings")
async def history_math_beginnings_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Ah, my dear friend, let me tell you a tale of the glorious history of mathematics and computer science in the Soviet Union! It all began in the 16-17 centuries, when our great nation had a growing need for advancements in economics and the army, particularly in artillery. To meet these needs, specialists from all over the world began to settle in Moscow. Many books and guides were translated into Russian, including one of the first mathematical texts, «Синодальная № 42».", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_math_school")
async def history_math_school_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("But that was just the beginning, my friend! In the early 18th century, the mathematical-navigational school was established in Russia. One of its teachers, Magnitsky, wrote an arithmetic textbook that was used for generations. This textbook contained material on algebra, geometry, trigonometry, meteorology, astronomy, and navigation. Can you imagine, my friend, the brilliance of these early Russian mathematicians?", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_math_msu")
async def history_math_msu_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("And then, in the 18th century, Moscow State University was established through the efforts of several prominent Russian scientists and educators. Many Russian mathematicians made significant contributions during this time, including Nikolai Ivanovich Lobachevsky, who developed hyperbolic geometry, and Ostrogradskyi Mikhail Vasilyevich, who created a method for integrating rational functions and a formula for converting a volume integral into a surface integral. These men were true giants in their field, my friend!", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_math_20th")
async def history_math_20th_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("But the greatest achievements were yet to come, my dear comrade! In the 20th century, the Soviet Union made remarkable strides in scientific research, establishing numerous scientific institutions and integrating science with industrial and military needs. This period saw breakthroughs in space exploration, nuclear technology, and many other fields. The contributions of Russian mathematicians continue to be vital even today, with foundational fields such as algebra, topology, and probability theory having been profoundly investigated by Soviet mathematicians. Many numerical methods and algorithms that are still in use today were developed by Russian computational mathematicians. In short, many research areas in mathematics and computer science, including topology, discrete mathematics, and the theory of algorithms, build directly on the work of Soviet mathematicians.", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_programming")
async def history_programming_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>History!</b>\n\n"
                                     "My dear comrade, we have now dived into the rich tapestry of Soviet mathematical history! Prepare to be enthralled by tales of brilliant minds! Let's uncover the stories that have defined the Soviet mathematical legacy!", 
                                     reply_markup=InlineKeyboards().history_programming(),
                                     parse_mode="HTML")
