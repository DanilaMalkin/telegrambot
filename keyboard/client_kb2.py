from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


c1 = KeyboardButton('Nike')
c2 = KeyboardButton('Adidas')



kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)



kb_client2.row(c1, c2)