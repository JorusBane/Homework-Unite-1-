from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Рассчитать"),
        KeyboardButton(text="Информация")
    ],
    [
        KeyboardButton(text="Купить")
    ]
    ], resize_keyboard=True)

product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Продукт 1", callback_data='product_buying'),
        InlineKeyboardButton(text="Продукт 2", callback_data='product_buying'),
        InlineKeyboardButton(text="Продукт 3", callback_data='product_buying'),
        InlineKeyboardButton(text="Продукт 4", callback_data='product_buying'),
        ]
    ], resize_keyboard= True )

