import telebot
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    greet = f'Привет, {message.from_user.first_name}, что тебе надо?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    convert1 = types.KeyboardButton('Конвертировать рубли в сомы')
    convert2 = types.KeyboardButton('Конвертировать сомы в рубли')
    course = types.KeyboardButton('Узнать курс')
    markup.add(convert1, convert2, course)
    bot.send_message(message.chat.id, greet, reply_markup=markup)
@bot.message_handler()
def valuta(message):
    if message.text == 'Узнать курс':
        bot.send_message(message.chat.id, 'Погугли')
    else:
        bot.send_message(message.chat.id, 'Сколько?')





bot.polling(none_stop=True)