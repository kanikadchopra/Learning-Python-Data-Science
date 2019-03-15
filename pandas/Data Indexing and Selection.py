import numpy as np
import pandas as pd
import string

# Data Indexing and Selection
# Topics Covered:
# 1. Data Selection in Series
# 2. Data Selection in DataFrame

# 1. Data Selection in Series
# Series as dictionary
alphabet = list(string.ascii_lowercase)

data = pd.Series(np.arange(0.1, 1.1,0.1), index=alphabet[:10])
print('data[b]:', data['b'])
print('is a in data?:', 'a' in data)
data.keys()
list(data.items())

print("Old data:")
print(data)
data['k'] = 1.1
print("New data:")
print(data)

# Series as a on-dimensional array
data['a':'c'] # slicing by explicit index
data[0:2] #slicing by implicit integer index
data[(data>0.4) & (data<0.9)] # masking
data[['a', 'h', 'k']] # fancy indexing

# 2. Data Selection in DataFrame
# a) DataFrame as a dictonary of Series structures
weight = pd.Series({'Mary': 152.0, 'John': 170.5, 'Calvin': 166.5, 'Harris': 175.5})
height = pd.Series({'Mary': 55, 'John': 83, 'Calvin': 64, 'Harris': 69})
data = pd.DataFrame({'weight': weight, 'height':height})

#  Dictionary-style indexing
data['weight']

# Attribute-style indexing
data.weight

# Adding in BMI
w = data['weight'] * 0.45
h = (data['height'] * 0.025) **2
data['bmi'] = w/h

# DataFrame as 2D array
# Weight & Height of first three people:
data.iloc[:3, :2]

# Another way to access the same data
data.loc[:'Calvin', :'height']