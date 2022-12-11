import telebot # импорт библиотеки
from telebot import types #можно это не писать, но придется везде писать перед types 'telebot.'
   # пустая строка отделяет стандартные библиотеки от пользовательских
import valut4ik_bot.converter as converter #мы в корневой папке, импортируем converter из папки valut4ik_bot, точка значит, что мы идем внутрь
from config import BOT_TOKEN
from resources import *


bot = telebot.TeleBot(BOT_TOKEN)
converter = converter.Converter()


@bot.message_handler(commands=['start'])
def start(message):
    greet = f'Привет, {message.from_user.first_name}, жми кнопку'
    markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=2,
            one_time_keyboard=False
            )
    markup.add(
            types.KeyboardButton(RUB_SOM_BTNTXT),
            types.KeyboardButton(SOM_RUB_BTNTXT),
            types.KeyboardButton(ASK_RATE_BTNTXT),
            )
    bot.send_message(message.chat.id, greet, reply_markup=markup)


@bot.message_handler(content_types='text')
def valuta(message):
    if message.text == ASK_RATE_BTNTXT:
        bot.send_message(
                message.chat.id,
                f'За 1 рубль нынче дают {converter.one_rub_in_kgs()} сом'
                )
    elif message.text == RUB_SOM_BTNTXT:
        msg = bot.reply_to(message, 'Сколько?')
        bot.register_next_step_handler(msg, rub_to_som)
    elif message.text == SOM_RUB_BTNTXT:
        msg = bot.reply_to(message, 'Сколько?')
        bot.register_next_step_handler(msg, som_to_rub)


def rub_to_som(message):
    try:
        amount = float(message.text)
        converted_amount = converter.rub_to_kgs(amount)
        bot.reply_to(message, converted_amount)
    except converter.ConversionError:
        bot.reply_to(message, 'Чё-то не смог посчтитать...')


def som_to_rub(message):
    try:
        amount = float(message.text)
        converted_amount = converter.kgs_to_rub(amount)
        bot.reply_to(message, converted_amount)
    except converter.ConversionError:
        bot.reply_to(message, 'Чё-то не смог посчтитать...')


bot.infinity_polling()
