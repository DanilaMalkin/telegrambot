from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

e1 = KeyboardButton('High')
e2 = KeyboardButton('Mid')
e3 = KeyboardButton('Low')



kb_client4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client4.row(e1, e2).row(e3)




