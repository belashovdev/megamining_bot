import asyncio
from re import A
from aiogram import executor

from loader import dp, create_db, drop_db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispacter):
    await drop_db()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)