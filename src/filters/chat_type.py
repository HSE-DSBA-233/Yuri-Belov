"""
Chat Type Filters Module.

This module provides filters for handlers to set a chat type (Private/Group) based on the type of chat
provided in the message object.

Classes:
    ChatTypeFilter: Filter to check if the chat type matches the specified type(s).
"""

from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type
