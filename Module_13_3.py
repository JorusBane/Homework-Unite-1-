from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ""
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

WishesList = "File1"
with (open(WishesList, encoding='utf-8') as file):
    count = 0
    file_att = []
    for line in file:
        file_att.append(line)
        count += 1

counter = random.randint(0, count)


@dp.message_handler(commands= ["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

