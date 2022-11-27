# Valut4ik – Telegram bot for rubles/soms conversion

## Setup
1. Make venv and activate it
1. Install packages from `requirements.txt` using `pip install -r requirements.txt`
1. Create file `./venv/Lib/site-packages/_set_envs.pth` with content

    ```Python
    import os; os.environ['BOT_TOKEN'] = ''; os.environ['CONVERTER_API_TOKEN'] = ''
    ```
1. Fill empty values with corresponding keys
