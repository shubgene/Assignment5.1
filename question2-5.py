# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 22:56:27 2018

@author: shurastogi
"""

import numpy as np
import pandas as pd

#Question 2 Create a DatetimeIndex that contains each business day of 2015 and use it to index a
#Series of random numbers.
dataframe_time_index = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') 
series = pd.Series(np.random.rand(len(dataframe_time_index)), index=dataframe_time_index)
series

#Question 3 Find the sum of the values in s for every Wednesday
series[dataframe_time_index.weekday==2].sum()

#question 4 Average For each calendar month
series.resample('M').mean()

#Question 5 For each group of four consecutive calendar months in s, find the date on which the
#highest value occurred.
series.groupby(pd.Grouper(freq='4M')).idxmax()
