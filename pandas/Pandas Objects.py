import numpy as np
import pandas as pd 
import string

# Pandas Objects
# Topics Covered:
# 1. Series: changing index, creating from dictionary, indexing
# 2. DataFrame: Generalized arrays, from Dictionaries, Constructing (e.g. Series,
# list of dicts, structured array)
# 3. Index: immutable array, ordered set

# Series Object
data = pd.Series(np.arange(0.1,1.1,0.1))

first = data[0]
last = data[len(data)-1:]
every_other = data[::2]

# Changing the index
new_ind = list(string.ascii_lowercase[:len(data)])
data2 = pd.Series(np.arange(0.1,1.1, 0.1), index=new_ind)

# Creating from a dictionary
ages_dict = {'Amy': 21,
             'Frank': 20,
             'George': 19,
             'Fred': 22,
             'Sam': 18}

ages = pd.Series(ages_dict)

# Indexing: 
print("Sam's age:", ages['Sam'])
print("George to Sam's ages:", ages['George':'Sam'])


# DataFrame
# A generalized NumPy array
weight = {'Amy': 50.5,
             'Frank': 70.5,
             'George': 72.0,
             'Fred': 67.5,
             'Sam': 60.5}
people = pd.DataFrame({'age': ages, 'weight': weight})
print("Index:", people.index)
print("Cols:", people.columns)

# A specialized dictionary
print('Ages')
print(people['age'])
print('Weights')
print(people['weight'])

# Constructing DataFrame Objects
# From a single series:
age_data = pd.DataFrame(ages, columns=['age'])

# From a list of dicts
age_weight_dict = {'Amy': [21, 50.5],
             'Frank': [20, 70.5],
             'George': [19, 72.0],
             'Fred': [22, 67.5],
             'Sam': [18, 60.5]}

age_weight_data = pd.DataFrame(age_weight_dict, index=['Age', 'Weight']).T

# Filling in values 
missing_vals = pd.DataFrame([{'a': 1, 'b': 2}, {'b':3, 'c':4}])

# From a two-dimensional NumPy array
ex = pd.DataFrame(np.random.rand(3,2), columns=['foo', 'bar'], index =['a', 'b', 'c'])

# From a structured array
name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

data3 = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})

data3['name'] = name
data3['age'] = age
data3['weight'] = weight

dataframe3 = pd.DataFrame(data3)

# 3. Index
# Construct an index
ind = pd.Index([2,3,5,9,11])
ind[0] 
ind[::2]
print(ind.size, ind.shape, ind.ndim, ind.dtype)

# Index as an ordered Set
indA = pd.Index([1,2,3,6,8,10])
indB = pd.Index([2,3,4,5,7,9])

print("intersection:", indA & indB)
print("union:", indA | indB)
print("symmetric difference:", indA ^ indB)

# Another method
print("intersecton2:", indA.intersection(indB))
print("union2:", indA.union(indB))
