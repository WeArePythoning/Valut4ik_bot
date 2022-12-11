import os #модуль os нужен для действий на уровне оп.системы, например, удалить файл
import requests #библиотека для запросов по http

from config import CONVERTER_API_TOKEN


class Parser:

    def __init__(self): # при создании объектов этого класса метод init сразу выполнит следующие 2 строчки
        self.base_url = ('https://v6.exchangerate-api.com/v6/'
                f'{CONVERTER_API_TOKEN}/pair')
       # self.base_url = 'https://v6.exchangerate-api.com/v6/' + CONVERTER_API_TOKEN + '/pair' # /pair - это команда для этого API

    def get_exchange_rate(self, src, dst): #описывем метода, который принимает 2 аргумента (src - source, dst - destination)
        url = f'{self.base_url}/{src.upper()}/{dst.upper()}' #для получения курса нужно к base_url добавить имена валют, разделяя все слэшами
        try:
            data = requests.get(url).json() #модуль request, в нем функция get, принимающая url в качестве аргумента. Метод json конвертирует полученный json файл в нечто понимаемое питонов, вероятно, словарь
        except requests.RequestException: #если что-то пошло не так (ошибка сервера)
            raise ParseError #вызываем ошибку, которую назвали ParseError
        return data['conversion_rate'] # если нет ParseError, то функция возвращает значение для ключа 'conversion_rate' из json, полученного из API


class ParseError(Exception): # создали класс ошибок ParseError
    pass # наследуется от базового класса ошибок Exception  - встроенного (в __builtins__)


if __name__ == '__main__':
    parser = Parser()
    rate = parser.get_exchange_rate('USD', 'MNT')
    print(f'One dollar in tugriks: {rate}')
