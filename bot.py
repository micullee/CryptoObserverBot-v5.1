from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.reply("🤖 CryptoObserverBot v5.1 is live!\nI'll send you alerts, chart analysis and market patterns.")

if __name__ == '__main__':
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
