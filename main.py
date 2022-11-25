import telebot
from telebot import types
from valut4ik_bot.converter import Converter
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    greet = f'Привет, {message.from_user.first_name}, жми кнопку'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=False)
    convert1 = types.KeyboardButton('Рубли в сомы')
    convert2 = types.KeyboardButton('Сомы в рубли')
    course = types.KeyboardButton('Узнать курс')
    markup.add(convert1, convert2, course)
    bot.send_message(message.chat.id, greet, reply_markup=markup)
    
@bot.message_handler(content_types='text')
def valuta(message):
    if message.text == 'Узнать курс':
        bot.send_message(message.chat.id, f'За 1 рубль нынче дают {Converter().rub_to_kgs(1)} сом')
    elif message.text == 'Рубли в сомы':
        msg = bot.reply_to(message, 'Сколько?')
        bot.register_next_step_handler(msg, rub_to_som)
    elif message.text == 'Сомы в рубли':
        msg = bot.reply_to(message, 'Сколько?')
        bot.register_next_step_handler(msg, som_to_rub)
        
        
def rub_to_som(message):
    try:
        amount = message.text
        converted_amount = round(Converter().rub_to_kgs(float(amount)))
        bot.reply_to(message, converted_amount)
    except Exception as e:
        bot.reply_to(message, 'Чё-то не смог посчтитать...')
        
        
def som_to_rub(message):
    try:
        amount = message.text
        converted_amount = round(Converter().kgs_to_rub(float(amount)))
        bot.reply_to(message, converted_amount)
    except Exception as e:
        bot.reply_to(message, 'Чё-то не смог посчтитать...')
    
bot.infinity_polling()
    
