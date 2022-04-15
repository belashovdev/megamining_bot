from aiogram.dispatcher.filters.state import StatesGroup, State

class Mailing(StatesGroup):
    Text = State()

class EditPagePrice(StatesGroup):
    Text = State()
    Confirm = State()

class EditPageDelivery(StatesGroup):
    Text = State()
    Confirm = State()

class EditPageContact(StatesGroup):
    Text = State()
    Confirm = State()