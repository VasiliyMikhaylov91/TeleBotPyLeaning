import sqlite3

from aiogram import Bot, Dispatcher

import sys
sys.path.insert(1,'D:\GeekBrains')
from config import MY_BOT_TOKEN

from db_api import Database
bot = Bot(MY_BOT_TOKEN)
dp = Dispatcher(bot)
db_path = 'db_api\database\databaseshop.db'
db = Database(path=db_path)
try:
    db.create_table_users()
except sqlite3.OperationalError as e:
    print(e)
except Exeption as e:
    print(e)
try:
    db.create_table_products()
except sqlite3.OperationalError as e:
    print(e)
except Exeption as e:
    print(e)