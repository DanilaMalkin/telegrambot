from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboard import kb_client, kb_client2, kb_client3, kb_client4, kb_client6, kb_client7
from data_base import sqlite_db
from aiogram. types import InlineKeyboardMarkup, InlineKeyboardButton




# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет!🍀', reply_markup=kb_client)
        #await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/megekbot')

# @dp.message_handler(commands=['Режим_работы'])

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='VK', url='https://vk.com/memphis.logistics')
urlButton2 = InlineKeyboardButton(text='Telegram ', url='https://t.me/memphis_store')
urlkb.add(urlButton, urlButton2)

#dp.message handler (commands="ссылки")
async def url_command (message : types .Message):
    await message.answer ( "наши группы в:", reply_markup=urlkb)

async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'пн-пт с 12 до 19')

# @dp.message_handler(commands=['Расположение'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Романов переулок, 4с2')

# @dp.message_handler(commands=['Каталог_товаров'])
async def command_catalog(message: types.Message):
   await sqlite_db.sql_read(message)

async def command_catalog1(message: types.Message):
    await bot.send_message(
        message.from_user.id,
         'выберите Brand который хотите выбрать',
        parse_mode=types.ParseMode.HTML,
        reply_markup=kb_client7
    )

async def command_nike(message: types.Message):
   await sqlite_db.sql_read_nike(message)

async def command_adidas(message: types.Message):
   await sqlite_db.sql_read_adidas(message)

async def info(message: types.Message):
    await bot.send_message(message.from_user.id, 'отзывы о работе с нами\n•https://vk.com/shreckx?w=wall248557604_557%2Fall')

async def filtrr(message: types.Message):
    await bot.send_message(message.from_user.id, 'Nike - это мировой лидер в производстве спортивной обуви, одежды и аксессуаров. Они известны своим инновационным дизайном, высоким качеством и передовыми технологиями. Бренд Nike является символом спорта, активного образа жизни и стиля, и широко признан и популярен как среди профессиональных спортсменов, так и среди любителей активного образа жизни.', reply_markup=kb_client2)


async def podbornike(message: types.Message):
    await bot.send_message(message.from_user.id, '🛹<u><b>Nike Dunk</b></u> - это еще одна из популярных и узнаваемых моделей кроссовок от компании Nike. Оригинально выпущенные в 1985 году, они были разработаны как баскетбольная обувь, но впоследствии стали символом уличной моды.\n'
                                                 '🥂<u><b>Nike Air Force 1</b></u> - это легендарная модель кроссовок, выпускаемая компанией Nike. Она была впервые представлена в 1982 году и стала одной из самых популярных моделей в истории кроссовок.\n'
                                                 '🏀<u><b>Nike Jordan, также известный как Air Jordan</b></u>, представляет собой линию кроссовок и одежды, разработанную в сотрудничестве между брендом Nike и баскетбольной легендой Майклом Джорданом.',parse_mode=types.ParseMode.HTML, reply_markup=kb_client3)

async def podbornike1(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        '▪️<u><b>Высокие Nike Dunk (High)</b></u> имеют высокий верх, который подходит выше щиколотки. Они обеспечивают большую поддержку и защиту для голеностопного сустава. Высокие Данки часто имеют дополнительные элементы дизайна, такие как ремешки или дополнительные детали на верху, что делает их более заметными и стильными. \n\n'
        '▪️<u><b>Средние Nike Dunk (Mid)</b></u> представляют собой промежуточную версию между высокими и низкими моделями Nike Dunk. Они имеют среднюю высоту верха, которая располагается выше щиколотки, но ниже голеностопного сустава.\n\n'
        '▪️<u><b>Низкие Nike Dunk (Low)</b></u> напротив, имеют низкий верх, который заканчивается ниже щиколотки. Они обеспечивают большую свободу движения и более легкий и гибкий ощущения на ноге. Низкие Данки обычно имеют более минималистичный и классический дизайн.\n\n',
        parse_mode=types.ParseMode.HTML,
        reply_markup=kb_client4
    )
    photo_path1 = 'pictures/1.jpg'

    # Отправка фотографии
    with open(photo_path1, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

    photo_path2 = 'pictures/2.jpg'

    # Отправка фотографии
    with open(photo_path2, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

    photo_path3 = 'pictures/3.jpg'

    # Отправка фотографии
    with open(photo_path3, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'на фото по порядку все номерные <u><b>Jordan</b></u> , кликнете по номру о каких хотите узнать больше информации \n\n',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path4 = 'pictures/4.jpg'
    with open(photo_path4, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)



async def podborjordan1(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        '<u><b>Air Jordan 1</b></u>: Впервые выпущенная в 1985 году, Air Jordan 1 стала первой моделью бренда Jordan. Она имеет высокий верх и культовый дизайн, включая знаменитое крыло Air Jordan на боковой панели',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path5 = 'pictures/j1.jpg'
    with open(photo_path5, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan2(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 2: Представленная в 1986 году, Air Jordan 2 была разработана Брюсом Килгором. Она отличается элегантным и премиальным стилем, включая вышитые детали на верхней части и фирменный логотип на язычке.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path6 = 'pictures/j2.jpg'
    with open(photo_path6, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan3(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 3: Эта модель была представлена в 1988 году и разработана Тинкером Хэтфилдом. Air Jordan 3 стала первой кроссовкой бренда с видимой подошвой Air и знаменитым «Jumpman» логотипом на язычке.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path7 = 'pictures/j3.jpeg'
    with open(photo_path7, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan4(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 4: Представленная в 1989 году, Air Jordan 4 стала знаковой моделью благодаря своему стильному дизайну и инновационной технологии. Она имеет видимую подошву Air и детали сетчатой обивки.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path8 = 'pictures/j4.jpg'
    with open(photo_path8, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan5(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 5: Выпущенная в 1990 году, Air Jordan 5 разработана с учетом высокой производительности на баскетбольном поле. Она отличается зубчатой подошвой и вышитыми деталями на верхней части.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path9 = 'pictures/j5.jpg'
    with open(photo_path9, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan6(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 6: Представленная в 1991 году, Air Jordan 6 продолжала инновационные функции и стиль предыдущих моделей. Она имеет защитную капсулу на пятке и подошву с видимой технологией Air.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path10 = 'pictures/j6.jpg'
    with open(photo_path10, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan7(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 7: Впервые выпущенная в 1992 году, Air Jordan 7 отличается уникальным дизайном, включая графические детали и разноцветную подошву. Эта модель также была изначально предназначена для быстрого и выразительного стиля игры.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path11 = 'pictures/j7.jpg'
    with open(photo_path11, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan8(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 8: Представленная в 1993 году, Air Jordan 8 имеет ремешки по всей длине кроссовки для улучшенной поддержки и стабильности. Она также отличается уникальными графическими элементами и вышитыми деталями.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path12 = 'pictures/j8.jpg'
    with open(photo_path12, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan9(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 9: Эта модель была выпущена в 1993 году, когда Майкл Джордан временно ушел из баскетбола. Air Jordan 9 отличается минималистичным дизайном и вдохновлялась глобальными мотивами.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path13 = 'pictures/j9.jpeg'
    with open(photo_path13, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan10(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 10: Представленная в 1994 году, Air Jordan 10 была создана в честь 10-летней карьеры Майкла Джордана. Она имеет вышитые детали с именами городов, где играл Джордан, на подошве.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path14 = 'pictures/j10.jpg'
    with open(photo_path14, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan11(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 11: Впервые выпущенная в 1995 году, Air Jordan 11 стала одной из самых популярных и узнаваемых моделей. Она имеет элегантный дизайн с прозрачной подошвой и выразительными деталями.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path15 = 'pictures/j11.jpeg'
    with open(photo_path15, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

async def podborjordan12(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Air Jordan 12: Представленная в 1996 году, Air Jordan 12 была вдохновлена японскими кимоно. Она отличается текстурированной верхней частью и деталями, а также имеет низкую версию для повседневного использования.',
        parse_mode=types.ParseMode.HTML, reply_markup=kb_client6
    )
    photo_path16 = 'pictures/j12.jpeg'
    with open(photo_path16, 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

#@dp.message_handlers(lambda message: "как" in message.text)
async def order(message: types.Message):
    await bot.send_message(message.from_user.id, '1)выберете товар из нашего каталога\n2)напишите нашему менеджеру @Dsdo7')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(url_command, lambda message: "контакты" in message.text)
    dp.register_message_handler(open_command, lambda message: "режим" in message.text)
    dp.register_message_handler(place_command, lambda message: "расположение" in message.text)
    dp.register_message_handler(command_catalog, lambda message: "🕣All" in message.text)
    dp.register_message_handler(command_catalog1, lambda message: "каталог" in message.text)
    dp.register_message_handler(command_nike, lambda message: "🕒Nike" in message.text)
    dp.register_message_handler(command_adidas, lambda message: "🕐Adidas" in message.text)
    dp.register_message_handler(info, lambda message: "отзывы" in message.text)
    dp.register_message_handler(filtrr, lambda message: "подбор" in message.text)
    dp.register_message_handler(podbornike, lambda message: "Nike" in message.text)
    dp.register_message_handler(podbornike1, lambda message: "Dunk" in message.text)
    dp.register_message_handler(podborjordan, lambda message: "Jordan" in message.text)

    dp.register_message_handler(podborjordan1, lambda message: "🕑I" in message.text.upper().split())
    dp.register_message_handler(podborjordan2, lambda message: "🕐II" in message.text.upper().split())
    dp.register_message_handler(podborjordan3, lambda message: "🕒III" in message.text.upper().split())
    dp.register_message_handler(podborjordan4, lambda message: "IV" in message.text.upper().split())
    dp.register_message_handler(podborjordan5, lambda message: "V" in message.text.upper().split())
    dp.register_message_handler(podborjordan6, lambda message: "VI" in message.text.upper().split())
    dp.register_message_handler(podborjordan7, lambda message: "VII" in message.text.upper().split())
    dp.register_message_handler(podborjordan8, lambda message: "VIII" in message.text.upper().split())
    dp.register_message_handler(podborjordan9, lambda message: "IX" in message.text.upper().split())
    dp.register_message_handler(podborjordan10, lambda message: "X" in message.text.upper().split())
    dp.register_message_handler(podborjordan11, lambda message: "XI" in message.text.upper().split())
    dp.register_message_handler(podborjordan12, lambda message: "XII" in message.text.upper().split())

#🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣
    dp.register_message_handler(order, lambda message: "как" in message.text)
    #commands=['как_сделать_заказ']

#1 = I. 2 = II. 3 = III. 4 = IV. 5 = V. 6 =  V. 7 = VII. 8 = VIII. 9 = IX. 10 = X.