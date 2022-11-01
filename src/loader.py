import sqlite3
from pathLib import Path

from aiogram import Bot, Dispatcher

import sys
sys.path.insert(1,'G:\GeekBrains')
from config import MY_BOT_TOKEN

from db_api import Database
bot = Bot(MY_BOT_TOKEN)
dp = Dispatcher(bot)
db_path = Path('db_api', 'database', 'shop_database.db')
db = Database(path=db_path)
try:
    db.create_table_users()
except sqlite3.OperationalError as e:
    print(e)
except Exeption as e:
    print(e)