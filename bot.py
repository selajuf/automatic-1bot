import asyncio
import logging
from aiogram import Dispatcher

from handlers import bot_messages, user_commands, questionaire
from callbacks import pagination
from bot_instance import bot

logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
                    )

async def main():
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