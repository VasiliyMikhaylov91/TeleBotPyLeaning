import sys
sys.path.append('D:\GeekBrains')
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import sys
sys.path.insert(1,'G:\GeekBrains')
from config import MY_BOT_TOKEN

bot = Bot(MY_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def answer_start_comand(message: types.Message):
    await message.answer(text=f'Привет!'
                                f'\nЯ немножко тупенький, мало что умею...')

@dp.message_handler(commands='help')
async def answer_start_comand(message: types.Message):
    await message.answer(text=f'Список команд:\n/start для начала работы\n /help для получения справки')

@dp.message_handler()
async def answer_start_comand(message: types.Message):
    await message.answer(f'Привет! \n '
                       r'Напиши /help чтобы узнать как со мной общаться')

if __name__ == '__main__':
    executor.start_polling(dp)