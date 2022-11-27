import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CONVERTER_API_TOKEN = os.environ.get('CONVERTER_API_TOKEN')
