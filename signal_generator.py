# signal_generator.py - Fetches data and generates simple RSI/EMA signals

import requests
import pandas as pd
import pandas_ta as ta
from datetime import datetime
import config

def fetch_data():
    """Fetch latest 1-min forex data from Alpha Vantage."""
    url = f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=1min&apikey={config.ALPHA_VANTAGE_KEY}'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    if 'Time Series FX (1min)' not in data:
        return None
    
    # Convert to DataFrame (last 100 candles for RSI/EMA calc)
    df = pd.DataFrame.from_dict(data['Time Series FX (1min)'], orient='index')
    df = df.astype(float)
    df = df.sort_index(ascending=True)  # Oldest first
    df['close'] = df['4. close']
    return df

def generate_signal(df):
    """Compute RSI and EMA, generate buy/sell signal."""
    if df is None or len(df) < 20:  # Need enough data for indicators
        return "No data available."
    
    # Calculate indicators
    df['rsi'] = ta.rsi(df['close'], length=14)
    df['ema'] = ta.ema(df['close'], length=5)
    
    # Latest values
    latest_rsi = df['rsi'].iloc[-1]
    latest_close = df['close'].iloc[-1]
    latest_ema = df['ema'].iloc[-1]
    
    # Check market hours
    now = datetime.utcnow().hour
    if not (config.MARKET_OPEN_HOUR_UTC <= now < config.MARKET_CLOSE_HOUR_UTC):
        return "Market closed - no signals."
    
    # Simple rules
    if latest_rsi < 30 and latest_close > latest_ema:
        return f"Buy {config.PAIR} now! (RSI: {latest_rsi:.2f}, EMA: {latest_ema:.2f})"
    elif latest_rsi > 70 and latest_close < latest_ema:
        return f"Sell {config.PAIR} now! (RSI: {latest_rsi:.2f}, EMA: {latest_ema:.2f})"
    else:
        return "No signal - hold."

# For testing: print(generate_signal(fetch_data()))
