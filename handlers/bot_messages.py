from aiogram import Router, F
from aiogram.types import Message, FSInputFile, URLInputFile
from data.db import Database

from keyboards import reply, fabrics
from data.subloader import get_json

document = FSInputFile('data.json')
image = URLInputFile(
    "https://www.python.org/static/community_logos/python-powered-h-140x182.png",
    filename="python-logo.png"
)
db = Database('databasedb.db')
router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json("festivali.json")

    if msg == "актуальные мероприятия":
        await message.answer(f"<a href='{smiles[0][0]}'>{smiles[0][1]}</a> (тут встроил ссылку фотки в текст, надеюсь так можно)", reply_markup=fabrics.paginator())
    elif msg == "предыдущие эфиры":
        await message.answer('Предыдущие эфиры ((последний эфир)\n\nhttps://i.pinimg.com/originals/bd/65/3f/bd653fd51a79ee062d8fa5ac6e78dff8.jpg - первый формат отправки фотки')
        await message.answer_photo(image, 'или так')
    elif msg == "забрать подарки":
        await message.answer_document(document)
    elif msg == "профиль":
        await message.answer(f'Ваш профиль:\n\nрефка - https://t.me/fsdgsabot?start={message.from_user.id}\nВсего юзеров приглашено - {db.count_referrals(message.from_user.id)}')
    elif msg == "назад":
        await message.answer("Вы перешли в главное меню!", reply_markup=reply.main)
