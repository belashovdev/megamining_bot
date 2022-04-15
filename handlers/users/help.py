from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db
from keyboards.default import menu

@dp.message_handler(text="🚛 Доставка и оплата")
@dp.message_handler(commands=['delivery'])
async def delivery_help(message: types.Message):
    keyword = "delivery"
    page = await db.get_page(keyword)

    await message.answer(page.text, reply_markup=menu)