from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Актуальные мероприятия"),
            KeyboardButton(text="Предыдущие эфиры"),
            KeyboardButton(text="Забрать подарки"),
            KeyboardButton(text="Профиль")
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

rmk = ReplyKeyboardRemove()