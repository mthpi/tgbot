from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


b1 = InlineKeyboardButton(text='ЮKassa', callback_data="sub")
keyboard_sub = InlineKeyboardMarkup(row_width=1)

keyboard_sub.insert(b1)