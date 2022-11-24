import os
import requests


API_KEY = os.environ['EXCHANGE_RATE_API_KEY']


class Parser:

    def __init__(self):
        self.base_url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair'

    def get_exchange_rate(self, src, dst):
        url = f'{self.base_url}/{src.upper()}/{dst.upper()}'
        data = requests.get(url).json()
        return data['conversion_rate']


if __name__ == '__main__':
    parser = Parser()
    rate = parser.get_exchange_rate('USD', 'MNT')
    print(f'One dollar in tugriks: {rate}')
