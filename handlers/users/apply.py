from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from states import Order
from keyboards.default import menu, go_back
from utils.notify_admins import order_notify

@dp.message_handler(text="📨 Оставить заявку")
@dp.message_handler(commands=['order'])
async def order(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(f"*Оставить заявку*\n\n"
                         f"Отправьте боту ваше имя и номер телефона для связи (например: Игорь, 89991232233).\n"
                         f"Мы свяжемся с вами для уточнения деталей\n", reply_markup=go_back)

    await Order.Order1.set()


@dp.message_handler(state=Order.Order1)
async def answer_order(message: types.Message, state: FSMContext):
    contact = message.text

    if contact == "⬅️ Отмена":
        from handlers.users.start import register_user
        await state.finish()
        return await register_user(message)
        
    else:
        await db.add_new_order(contact)

        user_id = types.User.get_current().id
        user_name = types.User.get_current().full_name
        admin_notify = "Заявка: {} \nОт пользователя [{}](tg://user?id={})".format(contact, user_name, user_id)
        await order_notify(dp, admin_notify)
        
        await message.answer(f"Ваши данные: {contact}\n"
                         f"Спасибо, мы очень скоро вам перезвоним!\n", reply_markup=menu)

        await state.finish()



