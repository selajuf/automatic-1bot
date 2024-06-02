import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers import bot_messages, user_commands, questionaire
from callbacks import pagination

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

telegram_token = os.getenv("TELEGRAM_TOKEN")


async def main():
    bot = Bot(token=telegram_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('запущен')
    asyncio.run(main())