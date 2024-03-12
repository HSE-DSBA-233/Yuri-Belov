from aiogram import Router, types, F
from utils.logging import handler
from keyboards.inline.programming import InlineKeyboards
from filters.chat_type import ChatTypeFilter
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from states.programming_state import ProgrammingState
from openai import OpenAI
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from data.config import conf
from utils.db import db

programming_translator_router = Router(name='programming_tasks')
programming_translator_router.message.filter(ChatTypeFilter(chat_type=["private"]))

# translator
def programming_translator():
    # client = OpenAI(api_key=conf.openai_api_key)
    # response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "system", "content": "Ты - переводчик с современного языка программирования на советский."},
    #     {"role": "user", "content": "Who won the world series in 2020?"},
    #     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    #     {"role": "user", "content": "Where was it played?"}
    # ]
    # )
    # return response.choices[0].message.content

    soviet_language = "REFAL"
    code = 'def main():\n\tprint("Hello world")'
    client = MistralClient(api_key=conf.mistral_api_key)
    messages = [
        ChatMessage(role="system", 
                    content="You're an experienced programmer with a vast knowledge of various programming languages and their syntaxes."
                    "You excel in translating code snippets from one language to another while retaining the original structure and style."
                    f"Your task is to translate a code snippet from a modern programming language to the Soviet programming language {soviet_language}." 
                    "The resulting code snippet should closely mimic the structure and style of the original code."
                    "Your response should only be in the form of code, without using any words."
                    f"Here is the code to translate: {code}"),
        ChatMessage(role="user", content=f'def main():\n\tprint("Hello world")'),
    ]
    chat_response = client.chat(model="mistral-large-latest", messages=messages)
    return chat_response.choices[0].message.content


@programming_translator_router.callback_query(F.data == "programming_translator")
async def programming_translator_handler(callback: types.CallbackQuery):
    handler(__name__, type=callback)
    wait_message = await callback.message.answer("Wait, please...")
    await callback.message.answer(programming_translator())
    await wait_message.delete()
