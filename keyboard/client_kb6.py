from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

z1 = KeyboardButton('🕑I')
z2 = KeyboardButton('🕐II')
z3 = KeyboardButton('🕒III')
z4 = KeyboardButton('IV')
z5 = KeyboardButton('V')
z6 = KeyboardButton('VI')
z7 = KeyboardButton('VII')
z8 = KeyboardButton('VIII')
z9 = KeyboardButton('IX')
z10 = KeyboardButton('X')
z11 = KeyboardButton('XI')
z12 = KeyboardButton('XII')
z13 = KeyboardButton('Jordan')


#1 = I. 2 = II. 3 = III. 4 = IV. 5 = V. 6 = VI. 7 = VII. 8 = VIII. 9 = IX. 10 = X.

kb_client6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


kb_client6.row(z1, z2, z3).row(z4, z5, z6).row(z7, z8, z9).row(z10, z11, z12).row(z13)