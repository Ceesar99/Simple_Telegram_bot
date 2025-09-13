# config.py - Keep your keys safe (add to .gitignore)

TELEGRAM_TOKEN = '8414457542:AAEpbDNb52CJ928EfW1cUT8kR1ZsS8fM6h0'  # From BotFather
ALPHA_VANTAGE_KEY = 'LA1OBXRGG71CFCLW'  # Free from alphavantage.co

# Trading pairs (4 regular for weekdays + 1 OTC for weekends)
PAIRS = ['EURUSD', 'GBPUSD', 'AUDUSD', 'USDJPY', 'EUROTC']  # EUROTC for OTC (weekend trading)

TIMEFRAME = '1min'  # 1-minute candles for all pairs
MARKET_OPEN_HOUR_UTC = 9  # Market open for regular pairs (Mon-Fri, UTC)
MARKET_CLOSE_HOUR_UTC = 16  # Market close for regular pairs (Mon-Fri, UTC)
OTC_WEEKEND_ONLY = True  # Restrict EUROTC signals to weekends only
