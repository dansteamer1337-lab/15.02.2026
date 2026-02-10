import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def calculate_expression(expression: str) -> str:
    #Пишем функцию для вычисления выражений с использованием библиотеки 're'
    return

@dp.message(Command("start"))
async def cmd_start(message: Message):
    #Реакция бота на '/start'
    #Используем билдер клавиатуры create_calc_keyboard()
    return

def create_calc_keyboard():
    #Вот тут наша клавиатура
    builder = InlineKeyboardBuilder()
    builder.button(text="🔄 Вычислить пример", callback_data="calculate_example")
    builder.button(text="📚 Примеры выражений", callback_data="show_examples")
    builder.adjust(1)
    return builder.as_markup()

@dp.callback_query(F.data == "calculate_example")
async def process_calculate_callback(callback: CallbackQuery):
    #Реакция на кнопку '🔄 Вычислить пример'
    
    await callback.answer()

@dp.callback_query(F.data == "show_examples")
async def process_examples_callback(callback: CallbackQuery):
    #Реакция на кнопку 📚 Примеры выражений
    #Используем массив строчек
    
    await callback.answer()

@dp.message(F.text)
async def process_expression(message: Message):
    expression = message.text.strip()
    
    if re.match(r'^[0-9+\-*/().\s]+$', expression):
        result = calculate_expression(expression)
        #Отвечаем пользователю: какое было выражение и результат вычисления

    else:
        await message.answer(
            "🤔 Это не похоже на математическое выражение.\n"
            "Попробуй отправить пример, например: 5*5 или 10+2\n\n"
            "Или используй кнопку ниже:",
            reply_markup=create_calc_keyboard()
        )

async def main():
    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
