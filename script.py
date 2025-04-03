import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_nifty50_data():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    session = requests.Session()
    response = session.get(url, headers=headers)
    data = response.json()
    return pd.DataFrame(data['data'])

def top_gainers_losers(df):
    df_sorted = df.sort_values(by='pChange', ascending=False)
    gainers = df_sorted.head(5)
    losers = df_sorted.tail(5)
    return gainers, losers

def below_52_week_high(df):
    df['below_52_high'] = ((df['yearHigh'] - df['lastPrice']) / df['yearHigh']) * 100
    return df[df['below_52_high'] >= 30].head(5)

def above_52_week_low(df):
    df['above_52_low'] = ((df['lastPrice'] - df['yearLow']) / df['yearLow']) * 100
    return df[df['above_52_low'] >= 20].head(5)

def top_30_day_performers(df):
    df_sorted = df.sort_values(by='perChange30d', ascending=False)
    return df_sorted.head(5)

def plot_gainers_losers(gainers, losers):
    plt.figure(figsize=(10, 5))
    stocks = list(gainers['symbol']) + list(losers['symbol'])
    changes = list(gainers['pChange']) + list(losers['pChange'])
    colors = ['green'] * 5 + ['red'] * 5
    
    plt.bar(stocks, changes, color=colors)
    plt.xlabel("Stocks")
    plt.ylabel("% Change")
    plt.title("Top 5 Gainers and Losers of the Day")
    plt.savefig("output/gainers_losers_chart.png")
    plt.show()

if __name__ == "__main__":
    df = fetch_nifty50_data()
    gainers, losers = top_gainers_losers(df)
    below_high = below_52_week_high(df)
    above_low = above_52_week_low(df)
    top_performers = top_30_day_performers(df)
    
    output_data = {
        "Top 5 Gainers": gainers[['symbol', 'pChange']].to_string(index=False),
        "Top 5 Losers": losers[['symbol', 'pChange']].to_string(index=False),
        "Stocks 30% Below 52-Week High": below_high[['symbol', 'below_52_high']].to_string(index=False),
        "Stocks 20% Above 52-Week Low": above_low[['symbol', 'above_52_low']].to_string(index=False),
        "Top 5 Performers in Last 30 Days": top_performers[['symbol', 'perChange30d']].to_string(index=False)
    }
    
    with open("output/nifty50_analysis.txt", "w") as file:
        for key, value in output_data.items():
            file.write(f"{key}:\n{value}\n\n")
    
    plot_gainers_losers(gainers, losers)
