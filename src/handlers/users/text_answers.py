from aiogram import types
from loader import dp

vegitables = ['редис', 'огурец', 'помидор']

@dp.message_handler(text=vegitables)
async def answer_veg_text(message: types.Message):
    await message.reply(f'У меня есть {message.text}')


@dp.message_handler()
async def answer_some_text(message: types.Message):
    await message.answer(f'Привет! \n '
                       r'Напиши /help чтобы узнать как со мной общаться')