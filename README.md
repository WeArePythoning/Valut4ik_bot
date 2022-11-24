# Valut4ik_bot

## Setup
1. Make venv and activate it
1. Install packages from `requirements.txt` using `pip install -r requirements.txt`
1. Create file `./venv/Lib/site-packages/_set_envs.pth` with content

    ```Python
    import os; os.environ['TELEGRAM_BOT_KEY'] = ''; os.environ['EXCHANGE_RATE_API_KEY'] = ''
    ```
1. Fill empty values with corresponding keys
