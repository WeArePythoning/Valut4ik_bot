import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CONVERTER_API_TOKEN = os.environ.get('CONVERTER_API_TOKEN')


def print_hello():
    print("hello!")
    
print_hello()


if __name__ == "__main__":
    ...
# end main