import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Bot tokenini kiriting
API_TOKEN = '7727547560:AAEXu3lMe05851MICZ3a5BhuK0z_qNw571k'

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start komandasi uchun handler
@dp.message()
async def start_handler(message: Message):
    if message.text == "/start":
        await message.answer("Salom! Men sizning Telegram botim.")
    elif message.text == "/help":
        await message.answer("Sizga qanday yordam bera olaman?")
    else:
        await message.answer(f"Siz yuborgan matn: {message.text}")

# Asosiy ishga tushirish funksiyasi
async def main():
    await dp.start_polling(bot)

# Botni ishga tushirish
if __name__ == "__main__":
    asyncio.run(main())