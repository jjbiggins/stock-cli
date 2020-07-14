#!/usr/bin/env python3

import sys

import pandas_datareader as pdr
import yfinance as yf
import pandas_datareader.data as web
import datetime
import requests_cache
from datetime import date

ticker = sys.argv[1]
print(ticker)
print('Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))
expire_after = datetime.timedelta(days=3)
session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)

startDate = '2009-10-20'
endDate = '2020-07-14'
stocktick = ticker
start = startDate
end = endDate
goog = pdr.DataReader(stocktick, "yahoo", start, end, session=session)
'''
goog = yf.Ticker(ticker)
'''
print(goog)
