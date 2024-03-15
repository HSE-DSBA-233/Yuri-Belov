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
    await callback.message.edit_text("In the 16-17th centuries, the government needed to improve the level of education. Specialists from many countries began to settle in Moscow and a lot of books and guides were translated to Russian. Then, in the 18th century, when the mathematical-navigational school was established Peter the First asked Magnitsky to create an arithmetics textbook, which was used to teach several next generations. Also, the textbook contained material on algebra, geometry, trigonometry, meteorology, astronomy and navigation. As a fact, in 1755, by the initiative of Mikhail Lomonosov, Moscow State University was established. Chances are, you have probably heard the names of Euler and Bernoulli. Even though they were not Russian, they were invited to the Petersburg Science Academy where they taught the students. Euler even ended up learning Russian and several of his works were first released in Russian, and then in other languages. Also in that century, many Russian mathematicians reached their biggest achievements. Nikolai Lobachevsky did pioneering work on hyperbolic geometry, paving the way for significant advancements in various scientific disciplines. Mikhail Ostrogradsky developed a method for integrating rational functions and a formula for converting a volume integral into a surface integral, in fact, his method is even taught in our course of calculus.", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_math_ussr")
async def history_math_school_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("After the revolution struck, people did not forget about enlightenment. The Soviet Union's investigation in science was truly remarkable. The USSR managed to establish numerous scientific institutions, and integrate science with industrial and military needs. The first ever man in space was the Soviet citizen, Yuri Gagarin. And the nuclear technologies were developed very rapidly, compared to the rest of the world. Contributions of Russian mathematicians are vital even today in the entire world. Foundational fields of math such as algebra, topology, and probability theory were profoundly investigated by Soviet minds. Many numerical methods and algorithms that are still in use today were fulfilled by Soviet computational mathematics. It would be fair to say that these scientists were amongst the ones who laid the foundations of math and computer science as we know it today.\n\n"
                                     "The schooling system included lots of math and science. One of the reasons was that the USSR needed lots of specialists to develop its own technologies, because it was almost isolated from the rest of the world. It is also important to note, that in soviet society being a man of science was highly respected and the Soviet scientific community was very well organized.\n\n"
                                     "If we start talking about all the important scientists in the USSR in detail, this text will take up tens of pages. So, to have at least one example, here is a story of just one of many of great Soviet minds.",
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_math_msu")
async def history_math_msu_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("And then, in the 18th century, Moscow State University was established through the efforts of several prominent Russian scientists and educators. Many Russian mathematicians made significant contributions during this time, including Nikolai Ivanovich Lobachevsky, who developed hyperbolic geometry, and Ostrogradskyi Mikhail Vasilyevich, who created a method for integrating rational functions and a formula for converting a volume integral into a surface integral. These men were true giants in their field, my friend!", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_math_pontryagin")
async def history_math_20th_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Lev Semenovich Pontryagin epitomizes the quintessence of Soviet mathematical prowess, standing as a colossus in the annals of 20th-century mathematics. His intellectual endeavors not only sculpted the edifice of mathematics within the USSR but also left an indelible mark on the global scientific tapestry. Delving into the realm of topology, Pontryagin's seminal contributions, particularly in algebraic topology, have been nothing short of revolutionary. He was the architect behind the theory of characteristic classes, a cornerstone concept that elucidated the intricate interplay between the algebraic attributes of topological spaces and their geometrical configurations. This groundbreaking work has permeated through diverse fields, enriching differential geometry and knot theory with its profound insights. The 1950s heralded Pontryagin's development of the eponymous maximum principle, in collaboration with his disciples, a tour de force in the theory of optimal control. This principle unveiled a potent methodology for deciphering optimization quandaries, predominantly in dynamic systems. Its ramifications have profoundly impacted the domains of economics, engineering, and biology, redefining the boundaries of these disciplines.\n\n"
                                     "Beyond these realms, Pontryagin's forays into differential geometry and the theory of topological groups have significantly broadened the horizons of our understanding regarding the constitution and characteristics of a plethora of mathematical entities and spaces. His oeuvre stands as a testament to a mind that navigated the abstract dimensions of mathematics with unparalleled finesse and depth.", 
                                     reply_markup=InlineKeyboards().history_math())


@history_router.callback_query(F.data == "history_programming")
async def history_programming_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>History!</b>\n\n"
                                     "Ah, my dear friend, allow us to plunge into the vibrant world of Soviet programming, a realm filled with the intellectual prowess of our great comrades! Brace yourself for captivating narratives of ingenious minds who have left their indelible marks on our motherland's technological landscape! Together, let us unveil the chronicles that have shaped the very essence of Soviet programming heritage!", 
                                     reply_markup=InlineKeyboards().history_programming(),
                                     parse_mode="HTML")


@history_router.callback_query(F.data == "history_programming_part1")
async def history_programming_part1_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("The history of USSR programming goes down to 1940 - the year, when the key concepts of development of Informatics and Programming were laid.\n\n"
                                     "One of the most prominent individuals, who contributed to the USSR programming school, was Andrey Petrovich Ershov. Initially, he dreamt of becoming a physicist, but due to unexpected circumstances the twist of fate forced him to transfer from Physics faculty to Mathematics faculty. Out of spite, this future father of Soviet computer science attended one of the first programming lectures, conducted by Lyapunov Alexey Andreevich, hoping that he would receive just a tiniest bit of physics there. However, his path was already dictated then - he would become one of the first Soviet programmers.", 
                                     reply_markup=InlineKeyboards().history_programming(),
                                     parse_mode="HTML")


@history_router.callback_query(F.data == "history_programming_part2")
async def history_programming_part2_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Ershov had his influence both in revolutionary discoveries in programming and education of the Soviet Union. “Alpha”, the biggest computer science project at that time, quickly morphed into “Beta” - its promised successor, which development did not go according to plan at all. Nevertheless, “Beta” was eventually released, thus demonstrating the adaptability and flexibility of USSR programmers.\n\n"
                                     "Another figure worth mentioning is Vladimir Pentkovski. A talented computer scientist, graduate of MIPT, who was one of the main architects of the Soviet “Elbrus” supercomputers and the programming language El-76, developed specifically for this platform. After the USSR ceased to exist, he immigrated to the United States, where he started working for Intel. He developed an architecture for the Pentium III processor, and according to the popular legend, it was actually named after him.", 
                                     reply_markup=InlineKeyboards().history_programming(),
                                     parse_mode="HTML")
