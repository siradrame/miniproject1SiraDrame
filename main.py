# INF601 - Advanced Programming in Python
# Sira Drame
# Mini Project 1
import pprint

import yfinance as yf

mytickers = ['MSFT','AAPL', 'GOOGL', 'TSLA', 'AMZN']

for ticker in mytickers:
    result = yf.Ticker(ticker)
    print(f"Ticket: {ticker}  \tDay High: {result.info['dayHigh']}")
#msft.info [""]

# get historical market data
#hist = msft.history(period="10d")

#pprint.pprint(hist)