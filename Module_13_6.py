from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = ""
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())

Kb1 = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Рассчитать норму каллорий ', callback_data='calories')
button1 = InlineKeyboardButton(text='Формула рассчета', callback_data='formulas')
Kb1.add(button)
Kb1.add(button1)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text= ["Рассчитать"])
async def start(message):
    await message.answer('Выберите опцию.', reply_markup = Kb1 )

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.message_handler(commands= ["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.callback_query_handler(text= ["calories"])
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age= int(message.text))
    await message.answer(f"Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state= UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth= int(message.text))
    #date = await state.get_data()
    await message.answer(f"Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight= int(message.text))
    data = await state.get_data()
    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    await message.answer(f"Ваша норма каллорий {calories}")
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
