import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token="7236138991:AAHAecN8Rl4utPCtM3DhthdOsWcY8TWLqrA")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):

    await message.answer("Hello", reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text='ZAVOD',
            web_app=WebAppInfo(url='https://github.com/AnthonyRom12'))
    ]]))


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
