import telebot
from telebot import types

import valut4ik_bot.converter as converter
from config import BOT_TOKEN
from resources import BUTTON_NAMES


bot = telebot.TeleBot(BOT_TOKEN)
converter_obj = converter.Converter()


@bot.message_handler(commands=['start'])
def start(message):
    greet = f'Привет, {message.from_user.first_name}, жми кнопку'
    markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            row_width=2,
            one_time_keyboard=False
            )
    markup.add(
            types.KeyboardButton(BUTTON_NAMES['RUB_SOM_BTNTXT']),
            types.KeyboardButton(BUTTON_NAMES['SOM_RUB_BTNTXT']),
            types.KeyboardButton(BUTTON_NAMES['ASK_RATE_BTNTXT']),
            )
    bot.send_message(message.chat.id, greet, reply_markup=markup)


@bot.message_handler(content_types='text')
def valuta(message):
    if message.text == BUTTON_NAMES['ASK_RATE_BTNTXT']:
        bot.send_message(
                message.chat.id,
                f'За 1 рубль нынче дают {converter_obj.one_rub_in_kgs()} сом'
                )
    elif message.text == BUTTON_NAMES['RUB_SOM_BTNTXT']:
        msg = bot.reply_to(message, 'Сколько?')
        bot.register_next_step_handler(msg, rub_to_som)
    elif message.text == BUTTON_NAMES['SOM_RUB_BTNTXT']:
        msg = bot.reply_to(message, 'Сколько?')
        bot.register_next_step_handler(msg, som_to_rub)


def rub_to_som(message):
    try:
        amount = float(message.text)
        converted_amount = converter_obj.rub_to_kgs(amount)
        bot.reply_to(message, converted_amount)
    except (converter.ConversionError, ValueError):
        bot.reply_to(message, 'Чё-то не смог посчтитать...')


def som_to_rub(message):
    try:
        amount = float(message.text)
        converted_amount = converter_obj.kgs_to_rub(amount)
        bot.reply_to(message, converted_amount)
    except (converter.ConversionError, ValueError):
        bot.reply_to(message, 'Чё-то не смог посчтитать...')


bot.infinity_polling()
