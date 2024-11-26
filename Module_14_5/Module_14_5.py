from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from config import *
from keyboards import *
from texts import *
from crud_functions import *
from admin import *

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    sing_up = State()
    email = State()
    age = State()
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(start_work, reply_markup=kb)

@dp.message_handler(text=["Регистрация"])
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит)")
    await RegistrationState.sing_up.set()

@dp.message_handler(state=RegistrationState.sing_up)
async def set_username(message, state):
    if is_included(message.text):
        await message.answer("Пользователь с таким именем уже есть, введите другое имя")
        await RegistrationState.sing_up.set()
    else:
        await state.update_data(sing_up=message.text)
        await message.answer("Введите свой email")
        await RegistrationState.email.set()

@dp.message_handler(state= RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст")
    await RegistrationState.age.set()

@dp.message_handler(state= RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    add_user(data["sing_up"], data["email"], int(data["age"]))
    await state.finish()


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
    for i in range(1,5):
        with open(f'{i}.jpg', 'rb') as img:
            await message.answer_photo(img, products[i-1])
    # with open('2.jpg', 'rb') as img:
    #     await message.answer_photo(img, f"Название: creatine | Описание: {creatine} | Цена: 2000")
    # with open('3.jpg', 'rb') as img:
    #     await message.answer_photo(img, f"Название: protein | Описание: {protein} | Цена: 1500")
    # with open('4.jpg', 'rb') as img:
    #     await message.answer_photo(img, f"Название: amino_acid | Описание: {amino_acid} | Цена: 1000")
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
