from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from config import *
from keyboards import *
from texts import *

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(start_work, reply_markup=kb)


@dp.message_handler(text=["Рассчитать"])
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer(f"Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer(f"Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    await UserState.weight.set()
    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(f"Ваша норма каллорий {calories}")
    await state.finish()


@dp.message_handler(text="Купить")
async def get_buying(message):
    with open('1.jpg', 'rb') as img:
        await message.answer_photo(img, f"Название: bcaa | Описание: {bcaa} | Цена: 500")
    with open('2.jpg', 'rb') as img:
        await message.answer_photo(img, f"Название: creatine | Описание: {creatine} | Цена: 2000")
    with open('3.jpg', 'rb') as img:
        await message.answer_photo(img, f"Название: protein | Описание: {protein} | Цена: 1500")
    with open('4.jpg', 'rb') as img:
        await message.answer_photo(img, f"Название: amino_acid | Описание: {amino_acid} | Цена: 1000")
    await message.answer("Выберите продукт для покупки", reply_markup= product_kb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer(any_message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
