# config.py - Keep your keys safe (add to .gitignore)

TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'  # From BotFather
ALPHA_VANTAGE_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY_HERE'  # Free from alphavantage.co

# Trading pair and settings
PAIR = 'EURUSD'  # Example forex pair
TIMEFRAME = '1min'  # 1-minute data
MARKET_OPEN_HOUR_UTC = 9  # Filter: Only signal between these UTC hours
MARKET_CLOSE_HOUR_UTC = 16
