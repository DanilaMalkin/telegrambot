from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

d1 = KeyboardButton('Jordan')
d2 = KeyboardButton('Dunk')
d3 = KeyboardButton('Force')


kb_client3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client3.row(d1, d2).row(d3)




