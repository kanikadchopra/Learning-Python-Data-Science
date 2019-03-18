import numpy as np
import pandas as pd 

# Operating on Data in pandas:

# Topics Covered:
# 1. Ufuncs: Index Preservation
# 2. Ufuncs: Index Alignment - Series & DataFrames
# 3. Ufuncs: Operations Between DataFrame and Series


# 1. Index Preservation
rng= np.random.RandomState(42)
ser = pd.Series(rng.randint(0,10,4))

df = pd.DataFrame(rng.randint(0,10, (3,4)), columns = ['A','B', 'C', 'D'])

# Try a ufunc on the series:
np.exp(ser) 
# Preserves the indices so attempt on DataFrame
np.sin(df * np.pi /4)

# 2. Index Alignment 
# Series
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127}, name='population')

# To find population density:
print("Population Density:")
print(population/area)

# The indices in both population and area
area.index | population.index

# Using fill value
A = pd.Series([1,2,3], index =[0,1,4])
B = pd.Series([2,4,5], index=[1,4,5])

print("With NaN")
print(A+B)
print("Without NaN, default is 0")
print(A.add(B, fill_value=0))

# DataFrame
C = pd.DataFrame(rng.randint(0,20,(3,3)), columns=list('ABC'))
D= pd.DataFrame(rng.randint(0,10, (4,4)), columns=list('BACD'))
print("DataFrame with NaN")
print(C+D)


# 3. Operations Between DataFrame and Series
E = rng.randint(10, size=(3,4))
print("Subtract by first row")
print(E- E[0])

df = pd.DataFrame(E, columns=list('QRST'))
print("Row-wise subtraction")
print(df - df.iloc[0])

# Subtracting column wise
df.subtract(df['R'], axis=0)

halfrow = df.iloc[0, ::2] 
df - halfrow #Subtracting by only two columns