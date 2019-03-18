import numpy as np
import pandas as pd
import math

# Handling Missing Data
# Topics Covered:
# 1. Missing Data in pandas: Pythonic missing data, Missing numerical data, 
# NaN and None in Pandas
# 2. Operating on NULL values: Detecting, removing and replacing 

# 1. Missing Data in pandas
# Using None
vals1 = np.array([1,2, None, 4,5])

# Using NaN
vals2 = np.array([1,2, np.nan, 4,5])

# Calculating sum, min and max ignoring NaN
print("sum, min, max:")
print(np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2))

x = pd.Series(range(2), dtype=int)
x[0] = None

# 2. Operating on NULL values
data = pd.Series([1, 2, np.nan, 'watermelon', None])
# Check for nulls:
print('\n')
print("Any nulls?")
print(data.isnull())

# Choose only not nulls
print('\n')
print("Not null entries")
print(data[data.notnull()])

# For dataframes
df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [np.nan, 4,      6]])

print("Null entries")
print(df.isnull())
print('\n')
print("Not null entries")
print(df.notnull())

# Dropping null values
# Series
data.dropna()

# DataFrame
# Drop all rows with nulls:
df.dropna()
# OR 
df.dropna(axis='rows')
# OR 
df.dropna(axis=0)

# Drop all columns with nulls
df.dropna(axis='columns')
# OR 
df.dropna(axis=1)

# We change the third column to all nulls
df[3] = np.nan
# Drop the columns that have ALL nulls (so the third)
df.dropna(axis='columns', how='all')

# Using thresh to specify minimum number of non-null values
df.dropna(axis='rows', thresh=3)

# Dropping if it has majority nulls in row
row_len = len(df[0])
row_maj = math.ceil(row_len/2)
df.dropna(axis='rows', thresh=row_maj)

# Dropping if it has maojrity nulls in column
col_len = len(df)
col_maj = math.ceil(col_len/2)
df.dropna(axis='columns', thresh=col_maj)

# Filling Null Values
data3 = pd.Series([1,np.nan, 2, 3, None, 4], index=list('abcdef'))
# Fill it with zero
data3.fillna(0)
# Forward filling
data3.fillna(method='ffill')
# Back filling
data3.fillna(method='bfill')

# Forward filling on rows for DataFrames
df.fillna(method='ffill', axis=1)
