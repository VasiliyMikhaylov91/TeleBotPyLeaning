from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inlines.callback_data import navigation_items_callback
from loader import db


def get_item_inline_keyboard(id: int = 1) -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    left_id = id - 1
    right_id = id + 1
    btn_left = InlineKeyboardButton(text='<<<',
                                    callback_data=navigation_items_callback.new(
                                        for_data='items',
                                        id=left_id)
                                    )
    btn_right = InlineKeyboardButton(text='>>>',
                                     callback_data=navigation_items_callback.new(
                                         for_data='items',
                                         id=right_id)
                                     )
    if id == 1:
        item_inline_keyboard.add(btn_right)
    elif id == db.get_items_count('Products'):
        item_inline_keyboard.add(btn_left)
    else:
        item_inline_keyboard.row(btn_left, btn_right)
    return item_inline_keyboard
