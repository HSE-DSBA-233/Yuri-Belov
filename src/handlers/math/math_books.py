from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from utils.logging import handler
from aiogram.filters import StateFilter
from keyboards.inline.math import InlineKeyboards
from states.math_state import MathState
from filters.chat_type import ChatTypeFilter
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
import json
import random
from data.config import conf
from utils.db_math import db


math_books_router = Router(name='math_books')
math_books_router.message.filter(ChatTypeFilter(chat_type=["private"]))


# callback on theory button from, math menu
@math_books_router.callback_query(F.data == "math_theory")
async def math_handler_theory(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("<b>Theory!</b>\n\n"
                                     "Ah, splendid choice, dear friend! The realm of mathematical theory is a treasure trove of wisdom and beauty, waiting to be explored. Together, let's delve into the fascinating world of abstract concepts, theorems, and proofs that have shaped our understanding of mathematics, whay do you want to know more about?",
                                     reply_markup=InlineKeyboards().math_theory(),
                                     parse_mode="HTML")


# callback on history button from math menu
@math_books_router.callback_query(F.data == "math_books_lobby")
async def math_handler_books(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(text="Welcome to the enchanting world of mathematics, dear friend! To guide our journey through this captivating realm, please select an area of mathematics that piques your curiosity:", reply_markup=InlineKeyboards().math_books_lobby())


# callback on soviet math
@math_books_router.callback_query(F.data == "math_introduction")
async def math_handler_theory_introduction(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text(
        text=(
            f"<b>Differences in Soviet Mathematics from Global Mathematics:</b>\n\n"
            f"<b>Formalism and Rigor:</b>\n"
            f"The Soviet mathematical school emphasized a strict and formal approach to mathematics. Students studied mathematics with a focus on proofs and theoretical understanding, as opposed to the more applied or practical approach that might have been prevalent in other countries.\n\n"
            f"<b>Focus on Foundations:</b>\n" 
            f"Special attention was given to laying strong foundations of mathematical knowledge in the Soviet education system. A particular methodology was developed to foster the abilities of abstract thinking and logical analysis among schoolchildren.\n\n"
            f"<b>Integration with Physics and Other Sciences:</b>\n" 
            f"In Soviet schools and universities, an interdisciplinary approach was common, in which mathematics was closely intertwined with physics and other exact sciences. This created a deeper understanding of the connections between various fields of knowledge.\n\n"
            f"<b>Competitive Spirit:</b>\n" 
            f"The USSR had a well-developed system of mathematical Olympiads and competitions that fostered interest in mathematics among schoolchildren and students. These competitions also served as a platform for identifying and supporting gifted students.\n"
            ), 
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboards().math_introduction()
        )


"""
BOOKS SECTION
"""

#Fixtengolz
@math_books_router.callback_query(F.data == "math_book_analysis")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/1968Fixtengolz1-2_compressed.pdf"), caption="Математический анализ, Фихтенгольц")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_algebra")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/Kostrikin_A_I_-_Vvedenie_v_algebru_Chast_I_Osnovy_algebry_2000_FIZMATLIT_compressed.pdf"), caption="Введение в алгебру, Костринкин")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_geometry")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/TopologyAndGeometry.pdf"), caption="Основы общей топологии в задачах и упражнениях Архангельский, Пономарев")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_differential")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/Filippov-vvedenie-v-teoriyu-differencialnyh-uravnenij.pdf"), caption="А. Ф. Филиппов.\n Введение в теорию дифференциальных уравнений.")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_functions")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/Volkovyskiy_L_I__Lunts_G_L__Aramanovich_I_G_-_Sbornik_zadach_po_teorii_funktsiy_komplexnogo_peremennogo_-_2004_compressed.pdf"), caption="Задачник Волковыский по теории функций комплексного переменного")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_functionsAnalysis")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/FunctionalAnalysis.pdf"), caption="Функциональный анализ, Канторович")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_probability")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/ProbTheory_compressed.pdf"), caption="Курс теории вероятностей, Гнеденко")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_numberMethods")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/Samarskiy_1989_432_compressed.pdf"), caption="Численные методы, Самарский")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_discrete")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/discra_compressed.pdf"), caption="Дискретная математика для программистов, Новиков")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_logic")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/MATLOGIC.pdf"), caption="Математическая логика, Ершов, Полютин")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_diffGeometry")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/diffGeomp1.pdf"), caption="Лекции по диффференциальной геометрии Ч1, Тайманов")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/diffGeomp2.pdf"), caption="Лекции по диффференциальной геометрии Ч2, Тайманов")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_numberTheory")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/osnovy_teorii_chisel.pdf"), caption="Основы теории чисел, Винградов")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_optimization")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/Elsgolc1969ru_compressed.pdf"), caption="Дифферинциальные уравнения и Вариационное исчисление, Эльсгольц")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_managment")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/Managment.pdf"), caption="Проблемы управления")
    await msg.delete()


@math_books_router.callback_query(F.data == "math_book_physics")
async def send_pdf(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    msg = await callback.message.answer("I have a special book for this topic! Catch, I'm sending it your way...")
    await callback.message.answer_document(FSInputFile(path="assets/mathBooks/vladimirov-lectures-1981_compressed.pdf"), caption="Уравнение математический физики, Владимиров")
    await msg.delete()
"""
BOOKS SECTION
"""