import os
import requests
from config import CONVERTER_API_TOKEN


class Parser:

    def __init__(self):
        self.base_url = f'https://v6.exchangerate-api.com/v6/{CONVERTER_API_TOKEN}/pair'

    def get_exchange_rate(self, src, dst):
        url = f'{self.base_url}/{src.upper()}/{dst.upper()}'
        data = requests.get(url).json()
        return data['conversion_rate']


if __name__ == '__main__':
    parser = Parser()
    rate = parser.get_exchange_rate('USD', 'MNT')
    print(f'One dollar in tugriks: {rate}')
