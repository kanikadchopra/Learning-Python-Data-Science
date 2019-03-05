import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

# Fancy Indexing
# Topics to Cover:
# 1. Fancy Indexing Basics
# 2. Example: Selecting random points
# 3. Modifying Values with Fancy Indexing
# 4. Example: Binning Data

# 1. Fancy Indexing Basics
rand = np.random.RandomState(42)

x = rand.randint(100,size=10)

# Accessing three different elements:
print([x[4], x[3], x[0]])

# Or we can do this psasing a list of indices to obtain the same result
ind = [4,3,0]
print(x[ind])

## in multiple dimensions:
M = np.arange(12).reshape((3,4))
row = np.array([0,1,2])
col = np.array([2,1,3])
print("multi-fancy indexing:", M[row, col])

# 2. Example: Selecting random points 
mean = [0,0]
cov =[[1,2],   
      [2,5]]

X = rand.multivariate_normal(mean,cov,100)

plt.scatter(X[:,0], X[:, 1]);

# Use fancy indexing to select 20 random points 
# Choose 20 random indices with no repeats and then use these to select a portion 
# of the original array
indices = np.random.choice(X.shape[0], 20, replace=False)
selection = X[indices]

# Adding large over-plot circles at the locations of the selected indices
plt.scatter(X[:,0], X[:,1], alpha=0.3)
plt.scatter(selection[:,0], selection[:,1], facecolor='none', s=200);

#3. Modifying Values with Fancy Indexing 
x = np.arange(10)
i = np.array([2,5,1,3])
x[i] = 50
print("Altered x:", x)
x[i] -= 10
print("Sub 10 index:", x)
x[i] += 20
print("Add 20 index:", x)

# Repeated operations with modifying values with fancy indexing
i = [2,3,3,4,4,4]
x = np.zeros(10)
np.add.at(x, i, 1)
print(x)

# Example: Binning Data
np.random.seed(42)
x = np.random.randn(100)

# Compute a histogram by hand
bins = np.linspace(-5, 5,20)
counts = np.zeros_like(bins)

# Find the appropriate bin for each x
i = np.searchsorted(bins,x)

# Add 1 to each of these bins 
np.add.at(counts, i, 1)

#Plot the results
plt.plot(bins, counts, linestyle='steps')