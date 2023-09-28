from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

y1 = KeyboardButton('🕒Nike')
y2 = KeyboardButton('🕐Adidas')
y3 = KeyboardButton('🕣All')


kb_client7 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client7.row(y1, y2).row(y3)