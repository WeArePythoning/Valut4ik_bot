import os
from dotenv import load_dotenv #библиотека dotenv нужна для управления переменными среды


load_dotenv() #вызвали

BOT_TOKEN = os.environ.get('BOT_TOKEN') #функция получает имя переменной среды 'BOT_TOKEN' и возвращает ее значение, которое присваевается переменной BOT_TOKEN (названия сделали одинаковые)
CONVERTER_API_TOKEN = os.environ.get('CONVERTER_API_TOKEN')
