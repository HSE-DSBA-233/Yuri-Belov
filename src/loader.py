from aiogram import Bot
from data.config import conf

bot = Bot(token=conf.bot.token)

__all__ = ['bot']