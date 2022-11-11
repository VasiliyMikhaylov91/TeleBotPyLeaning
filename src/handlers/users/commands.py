from aiogram import types
from aiogram.types import InputFile, InputMediaPhoto

from keyboards import command_default_keyboard, command_delete_keyboard, get_item_inline_keyboard, \
    navigation_items_callback
from loader import dp, db


@dp.message_handler(commands='start')
async def answer_start_comand(message: types.Message):
    await message.answer(text=f'Привет!'
                              f'\nРад тебя видеть!!!',
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


@dp.message_handler(content_types=['contact'])
async def answer_contact_command(message: types.Message):
    if message.contact.user_id == message.from_user.id:
        await message.answer('Регистрация прошла успешно')
        db.add_user(int(message.from_user.id), str(message.contact.phone_number))
    else:
        await message.answer('Увы')


@dp.message_handler(commands=['product'])
@dp.message_handler(text=['Список товаров'])
async def answer_menu_command(message: types.Message):
    first_product_info = db.select_info('Products', id=1)
    first_product_info = first_product_info[0]
    _, name, prise, count, photo_path = first_product_info
    item_text = f'Название товара: {name}\n' \
                f'Цена товара: {prise}\n' \
                f'Количество товара: {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await message.answer_photo(photo=photo,
                               caption=item_text,
                               reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_items_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_info('Products', id=current_item_id)
    first_item_info = first_item_info[0]
    _, name, prise, count, photo_path = first_item_info
    item_text = f'Название товара: {name}\n' \
                f'Цена товара: {prise}\n' \
                f'Количество товара: {count}'
    photo = InputFile(path_or_bytesio=photo_path)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=item_text),
                                 chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 reply_markup=get_item_inline_keyboard(id=current_item_id))
