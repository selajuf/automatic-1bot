import json
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from utils.states import Form
from keyboards.reply import rmk

router = Router()

@router.message(Command("reg"))
async def fill_profile(message: Message, state: FSMContext):
    await state.set_state(Form.mail)
    await message.answer(
        "Давай начнем, введи свою почту",
        reply_markup=rmk
    )

@router.message(Form.mail)
async def form_name(message: Message, state: FSMContext):
    if '@' not in message.text:
        await message.answer("Введите корректную почту")
        return
    await state.update_data(mail=message.text)
    await state.set_state(Form.number)
    await message.answer("Отлично, теперь отправь свой номер телефона", reply_markup=rmk)

@router.message(Form.number)
async def form_age(message: Message, state: FSMContext):
    if any(char.isalpha() for char in message.text):
        await message.answer("Введите корректный номер телефона!")
        return
    await state.update_data(number=message.text)
    await state.set_state(Form.name)
    await message.answer(
            "Как тебя зовут?")

@router.message(Form.name)
async def form_photo(message: Message, state: FSMContext):
    if any(char.isdigit() for char in message.text):
        await message.answer("Введите корректное имя!")
        return
    await state.update_data(name=message.text, telegram_id=message.from_user.id, telegram_username=f'@{message.from_user.username}')
    data = await state.get_data()
    await state.clear()

    formatted_text = []
    [
        formatted_text.append(f"{key}: {value}")
        for key, value in data.items()
    ]
    print(formatted_text)

    with open('data.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

    await message.answer(
        "\n".join(formatted_text)
    )
