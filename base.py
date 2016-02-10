import numpy as np
import pandas as pd
from pandas_datareader import data

def get_data(ticker, src='yahoo', start='2/18/2006', end='4/14/2015'):
    return data.DataReader(ticker, data_source=src, start=start, end=end)

# Getting data
goog = data.DataReader('GOOG', data_source='google', start='2/14/2007', end='12/12/2015')
print(goog.tail())

# Sample Analytics
goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))
goog['Volatility'] = pd.rolling_std(goog['Log_Ret'], window=252) * np.sqrt(252)

# Basic Strategy Sample
sp500 = data.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', end='4/14/2014')
sp500['42d'] = np.round(pd.rolling_mean(sp500['Close'], window=42), 2)
sp500['252d'] = np.round(pd.rolling_mean(sp500['Close'], window=252), 2)

sp500['42-252'] = sp500['42d'] - sp500['252d']
SD = 50
sp500['Regime'] = np.where(sp500['42-252'] > SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252'] < -SD, -1, sp500['Regime'])
sp500['Regime'].value_counts()

# Daily Log Returns
sp500['Market'] = np.log(sp500['Close'] / sp500['Close'].shift(1))

# Today's returns
sp500['Strategy'] = sp500['Regime'].shift(1) * sp500['Market']

# sp500[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True, figsize=(8, 5))