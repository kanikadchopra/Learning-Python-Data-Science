import numpy as np

# # Topics Covered:
# 1. Example: Structured Arrays
# 2. Creating Structured Arrays
# 3. More Advanced Compound Types
# 4. RecordArrays

# 1. Example Structured Arrays
name = ['George', 'Michael', 'Susan', 'Fred', 'Jimmy']
age = [35, 23, 49, 43, 33]
weight = [61.5, 70.0, 56.5, 85.0, 68.0]

# Create a structured array with a compound data type to store this information
data = np.zeros(5, dtype={'names': ('name', 'age', 'weight'), 'formats': 
    ('U10','i4', 'f8')})
data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

# All Names
all_names = data['name']
last_name = data[-1]['name']

# Weight
all_weights = data['weight']
# Max weight
max_weight = np.max(data['weight'])
min_weight = np.min(data['weight'])
average_weight = np.average(data['weight'])
median_weight = np.median(data['weight'])
sorted_weights = np.sort(data['weight'])

# Get all ages 
all_ages = data['age']
max_age = np.max(data['age'])
min_age = np.min(data['age'])
average_age = np.average(data['age'])
median_age = np.median(data['age'])
sorted_ages = np.sort(data['age'])

# Names where age is under 30
under_30 = data[data['age']<30]['name']
# Above 30 but under 40
age_selection = data[(data['age']>30) & (data['age'] <40)]['name']

# 2. Creating Structured Arrays
np.dtype({'names': ('name', 'age', 'weight'), 'formats': 
    ('U10','i4', 'f8')})

# Classifying using NumPy dtypes
np.dtype(np.dtype({'names': ('name', 'age', 'weight'), 'formats': ((np.str_, 10), int, np.float32)}))

# Compound type specified as a list of tuples
np.dtype([('name', 'S10'), ('age', '<i4'), ('weight', 'f8')])

# 3. More Advanced Compound Types
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3,3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])

# 4. RecordArrays
data_rec = data.view(np.recarray)

# Age, weight, names
data_rec.age, data_rec.weight, data_rec.name

