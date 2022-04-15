from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db
from keyboards.default import menu

@dp.message_handler(text="📄 Прайс-лист")
@dp.message_handler(commands=['price'])
async def pricelist(message: types.Message):
    keyword = "pricelist"
    page = await db.get_page(keyword)

    await message.answer(page.text, reply_markup=menu)