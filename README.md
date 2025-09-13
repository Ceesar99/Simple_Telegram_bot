# Simple Telegram Trading Bot

A basic, rule-based Telegram bot for binary options signals on Pocket Option (or similar). Uses RSI and EMA indicators for 70-85% potential accuracy in short-term trades. No AI, simple logic.

## Setup
1. Get keys:
   - Telegram bot token from BotFather.
   - Alpha Vantage API key (free) from https://www.alphavantage.co/.
2. Edit `config.py` with your keys.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`
5. In Telegram, message your bot: /start then /signal.

## How It Works
- Fetches 1-min data for EUR/USD.
- Computes RSI(14) and EMA(5).
- Signals: Buy if RSI < 30 and price > EMA; Sell if RSI > 70 and price < EMA.
- Filters for market hours.

## Disclaimer
This is for educational use. Trading involves risk—test on demo accounts. Accuracy not guaranteed; backtest yourself.

## Deployment
- Local: Just run it.
- Free online: Use Replit or Railway.app (upload files, set env vars for keys).# Simple_Telegram_bot
Main for the production of the simple trading bot 
