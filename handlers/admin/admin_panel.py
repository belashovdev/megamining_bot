from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from asyncio import sleep

from data import config

from loader import dp, db
from states import Mailing, EditPagePrice, EditPageDelivery, EditPageContact
from keyboards.default import menu, admin_menu, go_to_admin

@dp.message_handler(user_id=config.ADMINS, text="⚙️ Админка")
@dp.message_handler(user_id=config.ADMINS, commands=['admin'])
async def admin_panel(message: types.Message):
    count_users = await db.count_users()
    await message.answer(f"⚙️ Панель администратора \n\n"
                         f"Всего пользователей в боте: {count_users} \n"
                         f"Поздравляю, вы охуенны.", reply_markup=admin_menu)

# Хендлеры работы с заявками
@dp.message_handler(user_id=config.ADMINS, text="💌 Заявки")
async def admin_panel(message: types.Message):
    orders = await db.get_orders()

    all_order = ""
    for order in orders:
        user_id = str(order.user_id)
        referral = order.referral
        contact = order.contact
        date  = str(order.date)
        message_order = (f"*Заявка* от [{user_id}](tg://user?id={user_id}) \n"
                         f"{contact} \n"
                         f"_Дата: {date}_ \n\n")
        
        all_order += message_order

    await message.answer(f"Последние 20 заявок: \n\n"
                         f"{all_order}", reply_markup=admin_menu)


# Хендлеры работы с рассылкой
@dp.message_handler(user_id=config.ADMINS, text="📨 Рассылка")
async def mailing(message: types.Message):
    await message.answer("Пришлите текст рассылки", reply_markup=go_to_admin)
    await Mailing.Text.set()


@dp.message_handler(user_id=config.ADMINS, state=Mailing.Text)
async def mailing_start(message:types.Message, state: FSMContext):
    text = message.text
    if text == "⬅️ Отмена": 
        await admin_panel(message)
        await state.reset_state()
    else:

        await state.update_data(text=text)

        data = await state.get_data()
        text = data.get("text")
        await state.reset_state()
        users = await db.get_all_users()

        for user in users:
            try:
                await dp.bot.send_message(chat_id=user.user_id,
                                   text=text)
                await sleep(0.3)
            except Exception:
                pass
        await message.answer("Рассылка выполнена.", reply_markup=admin_menu)


# Хендлер работы со страницами
@dp.message_handler(user_id=config.ADMINS, text="📄 ред. прайс-лист")
async def edit_price(message: types.Message):
    page = await db.get_page('pricelist')

    await message.answer(page.text)
    await message.answer("Отправьте боту новый прайс-лист, если хотите его изменить", reply_markup=go_to_admin)
    await EditPagePrice.Text.set()

@dp.message_handler(user_id=config.ADMINS, state=EditPagePrice.Text)
async def edit_price_confirm(message:types.Message, state: FSMContext):
    text = message.text
    if text == "⬅️ Отмена": 
        await admin_panel(message)
        await state.reset_state()
    else:

        await state.update_data(text=text)
        data = await state.get_data()
        text = data.get("text")
        await state.reset_state()

        try:
            edit_page = await db.update_page('pricelist', text)
            await message.answer("Прайс-лист успешно изменен", reply_markup=admin_menu)
        except Exception:
            await message.answer("Во время редактирования произошла ошибка", reply_markup=admin_menu)


@dp.message_handler(user_id=config.ADMINS, text="🚛 ред. доставка и оплата")
async def edit_delivery(message: types.Message):
    page = await db.get_page('delivery')

    await message.answer(page.text)
    await message.answer("Отправьте боту новые данные, если хотите их изменить", reply_markup=go_to_admin)
    await EditPageDelivery.Text.set()

@dp.message_handler(user_id=config.ADMINS, state=EditPageDelivery.Text)
async def edit_delivery_confirm(message:types.Message, state: FSMContext):
    text = message.text
    if text == "⬅️ Отмена": 
        await admin_panel(message)
        await state.reset_state()
    else:

        await state.update_data(text=text)
        data = await state.get_data()
        text = data.get("text")
        await state.reset_state()

        try:
            edit_page = await db.update_page('delivery', text)
            await message.answer("Страница доставки и оплаты успешно изменена", reply_markup=admin_menu)
        except Exception:
            await message.answer("Во время редактирования произошла ошибка", reply_markup=admin_menu)


@dp.message_handler(user_id=config.ADMINS, text="📞 ред. контакты")
async def edit_contact(message: types.Message):
    page = await db.get_page('contact')

    await message.answer(page.text)
    await message.answer("Отправьте боту новые данные, если хотите их изменить", reply_markup=go_to_admin)
    await EditPageContact.Text.set()

@dp.message_handler(user_id=config.ADMINS, state=EditPageContact.Text)
async def edit_contact_confirm(message:types.Message, state: FSMContext):
    text = message.text
    if text == "⬅️ Отмена": 
        await admin_panel(message)
        await state.reset_state()
    else:

        await state.update_data(text=text)
        data = await state.get_data()
        text = data.get("text")
        await state.reset_state()

        try:
            edit_page = await db.update_page('contact', text)
            await message.answer("Страница контактов успешно изменена", reply_markup=admin_menu)
        except Exception:
            await message.answer("Во время редактирования произошла ошибка", reply_markup=admin_menu)



       