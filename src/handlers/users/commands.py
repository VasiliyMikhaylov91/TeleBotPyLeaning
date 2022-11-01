from aiogram import types

from keyboards import command_default_keyboard
from loader import dp



@dp.message_handler(commands='start')
async def answer_start_comand(message: types.Message):
    await message.answer(text=f'Привет!'
                                f'\nЯ немножко тупенький пока, мало что умею...', reply_markup=command_default_keyboard)

@dp.message_handler(commands='help')
async def answer_help_comand(message: types.Message):
    await message.answer(text=f'Список команд:\n/start для начала работы\n /help для получения справки')


@dp.message_handler(commands='add')
async def answer_add_comand(message: types.Message):
    await message.reply(text=f'Я не умею пока ничего добавлять')