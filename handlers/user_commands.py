import random

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет!\n\nРегистрация - /reg", reply_markup=reply.main)