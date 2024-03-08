"""Bot Main Module

This module sets up and starts the bot application.

Functions:
    start_bot: Asynchronous function to start the bot, initializes the bot, dispatcher, includes routers
               and starts polling updates.
"""

import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher, enums
from data.config import conf
from handlers import routers
from utils.logging import set_logger


async def start_bot() -> None:
    # Set up logging for capturing and storing informational messages 
    set_logger()
    logger.success("Bot is on.")

    # Initialize bot and dispatcher to create instances that will handle communication with the Telegram API 
    # and manage message routing and processing, respectively
    bot = Bot(token=conf.bot.token)
    dp = Dispatcher()

    # Include routers for handling different types of messages to ensure that incoming messages 
    # are properly routed and processed based on their types and contents
    for router in routers:
        dp.include_router(router)

    # Delete any existing webhook
    await bot.delete_webhook(drop_pending_updates=True)

    # Start listening for new updates from the Telegram API to ensure real-time interaction 
    # and synchronization with users' messages and actions
    await dp.start_polling(bot, dispatcher=dp)

    logger.warning("Bot is off.")


if __name__ == "__main__":
    # Start the bot asynchronously to ensure that it runs concurrently with other tasks 
    # and does not block the main execution thread, enabling efficient handling of incoming messages 
    # and responsiveness to user interactions.
    asyncio.run(start_bot())
