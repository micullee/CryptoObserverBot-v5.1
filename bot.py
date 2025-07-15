import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing from .env")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Comanda de pornire
@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: Message):
    await message.reply(
        "🚀 CryptoObserverBot v5.1 is live!\n"
        "I'll send you alerts, chart analysis, macro trends, and market patterns.\n\n"
        "Use /setalert or /latestnews to explore features."
    )

# Exemplu de alertă declanșată manual
@dp.message_handler(commands=["alert"])
async def send_alert(message: Message):
    await message.answer("⚠️ ETH has reached RSI > 80 on the daily chart! Possible reversal ahead.")

# Rulare bot
if __name__ == '__main__':
    print("🤖 Bot is running...")
    executor.start_polling(dp, skip_updates=True)
