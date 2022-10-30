from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


command_default_keyboard = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/help')
        ],
        [
            KeyboardButton(text='/add')
        ],
        [
            KeyboardButton(text='Подтвердить номер телефона',
                           request_contact=True)
        ]
    ], resize_keyboard= True
)