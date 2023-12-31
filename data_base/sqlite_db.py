import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('catalog.db')
    cur = base.cursor()
    if base:
        print('Всё кайф, братанчик')
    base.execute('CREATE TABLE IF NOT EXISTS catalog(img TEXT, brand TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO catalog VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM catalog').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'\nБренд: {ret[1]} \nМодель: {ret[2]}\nОписание: {ret[3]}\nЦена: {ret[-1]}')


async def sql_read_adidas(message):
    for ret in cur.execute("SELECT * FROM catalog WHERE brand = 'Adidas'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'\nБренд: {ret[1]} \nМодель: {ret[2]}\nОписание: {ret[3]}\nЦена: {ret[-1]}')

async def sql_read_nike(message):
    for ret in cur.execute("SELECT * FROM catalog WHERE brand = 'Nike'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'\nБренд: {ret[1]} \nМодель: {ret[2]}\nОписание: {ret[3]}\nЦена: {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM catalog').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM catalog WHERE name == ?', (data,))
    base.commit()