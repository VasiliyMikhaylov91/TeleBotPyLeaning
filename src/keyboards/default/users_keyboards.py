from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


command_default_keyboard = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/help')
        ],
        [
            KeyboardButton(text='/menu'),
            KeyboardButton(text='/dk'),
            KeyboardButton(text='/add')
        ],
        [
            KeyboardButton(text='Подтвердить номер телефона',
                           request_contact=True)
        ]
    ], resize_keyboard= True
)

command_delete_keyboard = ReplyKeyboardRemove()