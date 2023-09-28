from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

f1 = KeyboardButton('вернуться на главную')



kb_client5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client5.row(f1)




