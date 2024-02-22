import asyncio
from loguru import logger
import sys

from aiogram import Bot, Dispatcher, enums

from data.config import conf
from handlers import routers
from utils.logging import set_logger


async def start_bot() -> None:
    set_logger()
    logger.success("Bot is on.")

    bot = Bot(token=conf.bot.token)
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, dispatcher=dp)

    logger.warning("Bot is off.")


if __name__ == "__main__":
    asyncio.run(start_bot())
