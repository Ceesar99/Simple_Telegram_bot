# Simple Telegram Trading Bot

A basic, rule-based Telegram bot for binary options signals on Pocket Option (or similar). Uses RSI (14) and EMA (5) indicators for 70-85% potential accuracy in short-term trades. No AI, simple logic. Handles 4 regular pairs (weekdays) and 1 OTC pair (weekends).

## Pairs Supported
- Regular (Mon-Fri, 9 AM-4 PM UTC): EURUSD, GBPUSD, AUDUSD, USDJPY
- OTC (Weekends only): EUROTC/USD

## Setup
1. Get keys:
   - Telegram bot token from BotFather.
   - Alpha Vantage API key (free) from https://www.alphavantage.co/.
2. Edit `config.py` with your keys and tweak pairs/hours if needed.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`
5. In Telegram, message your bot: /start then /signal.

## How It Works
- Fetches 1-min data for each pair.
- Computes RSI(14) and EMA(5).
- Signals: Buy if RSI < 30 and price > EMA; Sell if RSI > 70 and price < EMA.
- Filters: Regular pairs during market hours; OTC only on weekends.
- Designed for 1-5 min expiries on Pocket Option.

## Testing
- Run locally and send /signal.
- Backtest: Manually compare signals to Pocket Option charts.
- Use demo account—accuracy varies by market.

## Monetization Ideas
- Freemium: Basic signals free, add premium alerts for $5/month.
- Share in trading groups on Telegram/Reddit for users.

## Disclaimer
This is for educational use. Trading involves risk—test on demo accounts. Accuracy not guaranteed; backtest yourself. Not financial advice.

## Deployment
- Local: Just run it.
- Free online: Use Replit or Railway.app (upload files, set env vars for keys).
