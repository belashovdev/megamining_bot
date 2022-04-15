from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp, db
from keyboards.default import menu

@dp.message_handler(text="📞 Контакты")
@dp.message_handler(commands=['contact'])
async def contact_info(message: types.Message):
    keyword = "contact"
    page = await db.get_page(keyword)

    await message.answer(page.text, reply_markup=menu)