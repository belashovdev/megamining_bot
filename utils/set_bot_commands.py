from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("price", "Прайс-лист"),
            types.BotCommand("contact", "Контакты"),
            types.BotCommand("order", "Оставить заявку"),
            types.BotCommand("delivery", "Доставка и оплата"),
        ]
    )
