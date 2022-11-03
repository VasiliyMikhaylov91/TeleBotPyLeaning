from aiogram import types

from keyboards import command_default_keyboard, command_delete_keyboard
from loader import dp



@dp.message_handler(commands='start')
async def answer_start_comand(message: types.Message):
    await message.answer(text=f'Привет!'
                                f'\nЯ немножко тупенький пока, мало что умею...',
                         reply_markup=command_default_keyboard)

@dp.message_handler(commands='menu')
async def answer_menu_comand(message: types.Message):
    await message.answer(text='ok', reply_markup=command_default_keyboard)

@dp.message_handler(commands='dk')
async def answer_dk_comand(message: types.Message):
    await message.answer(text='ok', reply_markup=command_delete_keyboard)

@dp.message_handler(commands='help')
async def answer_help_comand(message: types.Message):
    await message.answer(text=f'Список команд:\n'
                              f'/start для начала работы\n'
                              f'/menu для вызова кнопочек\n'
                              f'/dk для скрытия кнопочек\n'
                              f'/help для получения справки')

@dp.message_handler(commands='add')
async def answer_add_comand(message: types.Message):
    await message.reply(text=f'Я не умею пока ничего добавлять')

