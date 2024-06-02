from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    mail = State()
    number = State()
    name = State()