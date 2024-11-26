import asyncio, sqlalchemy
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import app.handlers
from database import models

bot = Bot(token='7985969894:AAF1ymEkRntwHU4wczg41bCyoU50hQnDKus')
dp = Dispatcher()
async def main():
    dp.include_router(app.handlers.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    models.execute_query(models.create_connection(models.path), models.create_users_table)
    models.execute_query(models.create_connection(models.path), models.create_visits_table)
    models.execute_query(models.create_connection(models.path), models.create_users_visits_table)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

# print(sqlalchemy.__version__) # - установлена и работает