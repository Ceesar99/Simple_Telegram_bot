# signal_generator.py - Fetches data and generates simple RSI/EMA signals for multiple pairs

import requests
import pandas as pd
import pandas_ta as ta
from datetime import datetime, timezone
import config

def fetch_data(symbol):
    """Fetch latest 1-min forex data from Alpha Vantage."""
    # Map EUROTC to EUR/USD for approximation (OTC uses similar data)
    base = 'EUR' if symbol == 'EUROTC' else symbol[:3]
    quote = 'USD'
    url = f'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={base}&to_symbol={quote}&interval={config.TIMEFRAME}&apikey={config.ALPHA_VANTAGE_KEY}'
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

def is_weekend():
    """Check if it's Saturday or Sunday (UTC)."""
    day = datetime.now(timezone.utc).weekday()  # 5 = Saturday, 6 = Sunday
    return day in [5, 6]

def generate_signal(df, pair):
    """Compute RSI and EMA, generate buy/sell signal for one pair."""
    if df is None or len(df) < 20:  # Need enough data for indicators
        return "No data available."
    
    # Calculate indicators
    df['rsi'] = ta.rsi(df['close'], length=14)
    df['ema'] = ta.ema(df['close'], length=5)
    
    # Latest values
    latest_rsi = df['rsi'].iloc[-1]
    latest_close = df['close'].iloc[-1]
    latest_ema = df['ema'].iloc[-1]
    
    # Filter for regular pairs: Only during market hours (Mon-Fri)
    if pair != 'EUROTC':
        now = datetime.now(timezone.utc)
        if now.weekday() > 4:  # Weekend: Skip regular pairs
            return f"Weekend - no signals for {pair}."
        hour = now.hour
        if not (config.MARKET_OPEN_HOUR_UTC <= hour < config.MARKET_CLOSE_HOUR_UTC):
            return f"Market closed - no signals for {pair}."
    
    # Filter for OTC pair: Only on weekends if flag is True
    if pair == 'EUROTC' and config.OTC_WEEKEND_ONLY and not is_weekend():
        return "OTC signals only on weekends."
    
    # Simple rules
    if latest_rsi < 30 and latest_close > latest_ema:
        return f"Buy {pair}/USD now! (RSI: {latest_rsi:.2f}, EMA: {latest_ema:.2f})"
    elif latest_rsi > 70 and latest_close < latest_ema:
        return f"Sell {pair}/USD now! (RSI: {latest_rsi:.2f}, EMA: {latest_ema:.2f})"
    else:
        return f"No signal for {pair} - hold."

def generate_signals():
    """Generate signals for all configured pairs."""
    signals = []
    for pair in config.PAIRS:
        df = fetch_data(pair)
        signal = generate_signal(df, pair)
        signals.append(signal)
    return "\n".join(signals)    latest_close = df['close'].iloc[-1]
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
