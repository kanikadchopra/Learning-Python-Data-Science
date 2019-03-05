import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
# Sorting Arrays
# Topics to Cover:
# 1. Fast Sorting in NumPy: np.sort and np.argsort
# 2. Partial Sorts: Partitioning 
# 3. Example: k-Nearest Neighbors
# 4. Aside: Big O Notation

# Selection Sort
def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

# Test 1:
x = np.array([4,3,6,8,2,7,5,10,9,1])
print("Sorted array:", selection_sort(x))

def bogosort(x): 
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x

# Test 1:
x = np.array([2,4,5,3,1])
print("Bogosorted array:", bogosort(x))

# 1. Fast Sorting in NumPy 
# Using np.sort to sort array without modifying input 
x = np.array([2,1,4,5,3])
np.sort(x)

# Modifying the array in place
x.sort()
print("Sorted x:" ,x)

# Sorting with Fancy Indexing 
x = np.array([2,3,4,1,5])
i = np.argsort(x)
print("Fancy sorting:", x[i])

# Sorting along rows or columns 
rand= np.random.RandomState(42)
X= rand.randint(0, 10,(4,6))
print(X)

# Sort each column of X
np.sort(X, axis=0)

# Sort each row of X
np.sort(X, axis=1)

# 2. Partial Sorts: Partitioning 
x = np.array([7,2,3,1,6,5,4])
np.partition(x,3)
np.partition(X,2, axis=1) 

# 3. Example: k-Nearest Neighbors
X = rand.rand(10,2)

# Scatter plot these values 
plt.scatter(X[:,0], X[:,1], s=100);

dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis,:,:]) ** 2, axis=-1)
differences = X[:, np.newaxis,:] - X[np.newaxis,:,:]
differences.shape

# Square the coordinate differences
sq_differences = differences ** 2
sq_differences.shape

# Sum the coordinate differences to get the squared distance
Dist_sq = sq_differences.sum(-1)
Dist_sq.shape 

# Nearest neighbors
nearest = np.argsort(dist_sq, axis=1)
print(nearest)

# Another method to find nearest neighbors
K=2
nearest_partition = np.argpartition(dist_sq, K+1, axis=1)

# Plot the connections
plt.scatter(X[:,0], X[:,1], s=100)

# Draw lines from each point to its two nearest neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # Plot a line from X[i] to X[j]
        # Use some zip magic to make it happen
        plt.plot(*zip(X[j], X[i]), color='black')
        
