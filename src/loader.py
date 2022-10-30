from aiogram import Bot, Dispatcher
import sys
sys.path.insert(1,'G:\GeekBrains')
from config import MY_BOT_TOKEN

bot = Bot(MY_BOT_TOKEN)
dp = Dispatcher(bot)