# INF601 - Advanced Programming in Python
# Sira Drame
# Mini Project 1
import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import copy

# Get today's date
today = datetime.now()

# Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=15)

mytickers = ['MSFT','AAPL', 'GOOGL', 'TSLA', 'AMZN']

mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)
    if len(last10days) == 10:
       maxlist = copy.copy(last10days)
       maxlist.sort()
       max_price = maxlist[-1]+10
       min_price = maxlist[0]-10
       myarray = np.array(last10days)
       plt.plot(myarray)
       plt.xlabel('Days Ago')
       plt.ylabel('Closing Price')
       plt.axis((9, 0, min_price, max_price))
       plt.title(f"{ticker} last 10 closing prices")
       plt.show()
    else:
        print('You  do not have 10 days of data and you only have {len(last10days)} days.')
