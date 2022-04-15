from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📄 Прайс-лист"),
            KeyboardButton(text="📨 Оставить заявку"),
        ],
        [   
            KeyboardButton(text="🚛 Доставка и оплата"),
            KeyboardButton(text="📞 Контакты"),
        ],

    ],
    resize_keyboard=True
)

go_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Отмена"),
        ]

    ],
    resize_keyboard=True
)