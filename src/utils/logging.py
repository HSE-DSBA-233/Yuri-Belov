"""
Logging Utilities.

This module provides utilities for setting up and handling logging in the bot application. 

Functions:
    set_logger: Sets up the logger configuration.
    handler: Logs information from user messages or callbacks.
"""

import typing
from loguru import logger
from aiogram import types


def set_logger() -> None:
    # Set up logger configuration, logs are stored in ./logs.log
    return logger.add(
        sink="./logs.log",
        enqueue=False,
        backtrace=False,
        catch=False,
    )


def handler(
        func,
        type: typing.Union[types.Message, types.CallbackQuery],
) -> None:
    
    """log info from user message/callback

    args:
        func: function name (__name__)
        **type: Message | CallbackQuery: user message/callback

    returns:
        something like this
        `datetime | INFO     | utils.log_info:message:6 - function_name from fullname (@username) id: user_id`
    """
    return logger.info(
        "{mes} from {fullname} (@{username}) id: {id}",
        mes=func,
        id=type.from_user.id,
        username=type.from_user.username,
        fullname=type.from_user.full_name,
    )