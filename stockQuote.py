#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : stockQuote.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 14.07.2020
# Last Modified Date: 14.07.2020
# Last Modified By  : Joe Biggins <jjbiggins@joebiggins.io>

import os
import sys
from sys import argv
from datetime import date
from datetime import datetime
from datetime import timedelta

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web


# os.environ['YEAR'] = str(datetime(now.year - 1, now.month, now.day, now.hour, now.minute, now.second))

def priceOverTime(ticker, startDate = str(date.today() - timedelta(days = 7)), endDate = str(date.today())):
	stocktick = ticker
	start = startDate
	end = endDate
	data = pdr.DataReader(stocktick, "yahoo", start, end)
	print(data)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		ticker = str(sys.argv[1])
		priceOverTime(ticker)
	else:
		priceOverTime('goog')
