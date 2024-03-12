from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from openai import OpenAI
from data.config import conf
from states.programming_state import ProgrammingTranslatorState
from aiogram.fsm.context import FSMContext

programming_translator_router = Router(name='programming_tasks')
programming_translator_router.message.filter(ChatTypeFilter(chat_type=["private"]))


def programming_translator(lang: str, code: str):
    try:
        refal_snippet = '$ENTRY Go {\n\t= <HelloWorld\\>;\n}\n\nHelloWorld {\n\t= "Hello, World!";'
        rapira_snippet = 'ПРОЦ СТАРТ()\n\tВЫВОД: "ЗДРАВСТВУЙ, МИР!";\nКНЦ;'
        el76_snippet = 'начало\n\tконст печ = позп (ацпу);\n\tстрока привет = "Привет, мир!";\n\tзапф (печ, привет)\nконец'
        if lang == "REFAL-5":
            snippet = refal_snippet
        elif lang == "EL-76":
            snippet = el76_snippet
        elif lang == "RAPIRA":
            snippet = rapira_snippet
        client = OpenAI(api_key=conf.openai_api_key)
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're an experienced programmer with a vast knowledge of various programming languages and their syntaxes."
                                        "You excel in translating code snippets from one language to another while retaining the original structure and style."
                                        f'Your task is to translate a code snippet from a modern programming language to the Soviet programming language "{lang}".'
                                        "The resulting code snippet should closely mimic the structure and style of the original code."
                                        "Your response should only be in the form of code, without using any words."},
            {"role": "user", "content": 'print("Hello world!")'},
            {"role": "assistant", "content": snippet},
            {"role": "user", "content": 'kwjedfjkej123'},
            {"role": "assistant", "content": "That's not a valid code snippet."},
            {"role": "user", "content": 'привет, как дела?'},
            {"role": "assistant", "content": "That's not a valid code snippet."},
            {"role": "user", "content": code},
        ]
        )
        return response.choices[0].message.content
    except Exception:
        return "error"

@programming_translator_router.callback_query(F.data == "programming_translator")
async def programming_translator_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    await callback.message.edit_text("Choose a soviet language:", reply_markup=InlineKeyboards().programming_translator())


@programming_translator_router.callback_query(F.data == "programming_translator_refal5")
async def programming_translator_refal5_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text("Enter your code snippet:", parse_mode="HTML")
    await state.set_state(ProgrammingTranslatorState.code)
    await state.update_data({"lang":"REFAL-5"})


@programming_translator_router.callback_query(F.data == "programming_translator_el76")
async def programming_translator_el76_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text("Enter your code snippet:", parse_mode="HTML")
    await state.set_state(ProgrammingTranslatorState.code)
    await state.update_data({"lang":"EL-76"})


@programming_translator_router.callback_query(F.data == "programming_translator_rapira")
async def programming_translator_rapira_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text("Enter your code snippet:", parse_mode="HTML")
    await state.set_state(ProgrammingTranslatorState.code)
    await state.update_data({"lang":"RAPIRA"})


@programming_translator_router.message(ProgrammingTranslatorState.code)
async def programming_translator_answer_handler(message: types.Message, state: FSMContext):
    handler(__name__, type=message)
    wait_message = await message.answer("Wait, please...")
    data: dict = await state.get_data()
    answer: str = message.text
    response = programming_translator(data['lang'], answer)
    if any(word in response for word in ["valid", "code"]):
        await message.answer("❌ That's not a valid code snippet.")
    elif response == "error":
        await message.answer("Technical issue, try again later, please.")
    else:
        await message.answer(f"Here is your translated code snippet:\n\n```{data['lang']}\n{programming_translator(data['lang'], answer)}```", 
                             reply_markup=InlineKeyboards().programming_translator_continue(),
                             parse_mode="MarkdownV2")
    await wait_message.delete()
    await state.clear()


@programming_translator_router.callback_query(F.data == "programming_translator_continue")
async def programming_translator_continue_handler(callback: types.CallbackQuery, state: FSMContext):
    handler(__name__, type=callback)
    await callback.message.edit_text("Choose a soviet language:", reply_markup=InlineKeyboards().programming_translator())
