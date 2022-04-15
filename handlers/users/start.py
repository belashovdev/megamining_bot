from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command

from loader import dp, db
from keyboards.default import menu


@dp.message_handler(text="⬅️ Главное меню")
@dp.message_handler(CommandStart())
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    referral = message.get_args()
    user = await db.add_new_user(referral=referral)
    # id = user.id
   
    await message.answer("""
Добро пожаловать в Aspirine.mining - профессиональный сервис по продаже, ремонту и обслуживанию майнингового оборудования.

Здесь вы можете найти всегда актуальный прайс-лист. Если возникли вопросы - вы всегда можете спросить \
у нашего менеджера, для этого посетите раздел "контакты". 

Наши преимущества: 
✅ Заказ от 1 единицы товара! 
✅ Свой инженерный отдел, который решит любые ваши технические вопросы.
✅ Съемка фото и видео перед отправкой.
✅ Всегда актуальные цены. 

Официальный канал: @aspirineasic
    """, reply_markup=menu)



