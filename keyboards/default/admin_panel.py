from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💌 Заявки"),
            KeyboardButton(text="📨 Рассылка"),
        ],
        [   
            KeyboardButton(text="📄 ред. прайс-лист"),
            KeyboardButton(text="🚛 ред. доставка и оплата"),
            KeyboardButton(text="📞 ред. контакты"),
        ],
        [
            KeyboardButton(text="⬅️ Главное меню"),
        ],
    ],
    resize_keyboard=True
)

go_to_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Отмена"),
        ],
    ],
    resize_keyboard=True
)
