# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:29:13 2018

@author: Eliud Lelerai
"""
import numpy as np
import pandas as pd

## Question 1:How-to-count-distance-to-the-previous-zero
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
izero = np.r_[-1, (df['X'] == 0).nonzero()[0]]
idx = np.arange(len(df))
df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1]

## Question 2: Create a DatetimeIndex that contains each business day of 2015 and use it to index a
## Series of random numbers.

Data_2015 = pd.date_range(start='2015-01-01', end='2015-12-31') 
Series = pd.Series(np.random.rand(len(Data_2015)), index=Data_2015)

## Question 3: Find the sum of the values in s(Series) for every Wednesday
Wednesday_Sum=Series[Data_2015.weekday == 2].sum() 

## Question 4:Average For each calendar month
Monthly_Mean=Series.resample('M').mean()

## Question 5:For each group of four consecutive calendar months in s, find the date on which the
## highest value occurred
Four_Monthly_grouped_Data=Series.groupby(pd.Grouper(freq= '4M')).idxmax()

