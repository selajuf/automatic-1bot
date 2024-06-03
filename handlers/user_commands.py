from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from data.db import Database
from bot_instance import bot
from keyboards import reply

router = Router()

db = Database('databasedb.db')

@router.message(CommandStart())
async def start(message: Message):
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        referrer_id = str(start_command[7:])
        if str(referrer_id) != "":
            if str(referrer_id) != str(message.from_user.id):
                db.add_user(message.from_user.id, referrer_id)
                try:
                    await bot.send_message(chat_id=referrer_id, text='Кто то перешел по твоей ссылке')
                except Exception as e:
                    print(f"{e}")
            else:
                db.add_user(message.chat.id)
                await message.answer("Нельзя зарегаться по своей ссылке")
        else:
            db.add_user(message.chat.id)

    await message.answer("Привет!\n\nРегистрация в файл data.json доступна через команду - /reg", reply_markup=reply.main)