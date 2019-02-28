import numpy as np

# THE BASICS OF NUMPY ARRAYS 
# Topics Covered: 
# 1) Attributes of Arrays: size, shape, memory consumption, data types
# 2) Indexing of arrays: Individual array elements
# 3) Slicing of arrays: Getting smaller subarrays within a larger array
# 4) Reshaping of arrays: Changin the shape of a given array
# 5) Joining and splitting of arrays: Combining arrays into one and splitting one
# into many 

# Creating arrays: 
zero_array = np.zeros(10, dtype=int) # Array with all zeros
one_matrix = np.ones((3,5), dtype=float) # Array with all ones
pi_matrix = np.full((3,5), 3.14) # Array with al pis
id_matrix3 = np.eye(3) # Identity matrix 3x3


np.random.seed(0)
x1 = np.random.randint(10, size=6)

x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

# 1) Attributes:
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
print("dtype: ", x3.dtype)
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")


# 2) Array Indexing
x1[0] # first element
x1[-1] # last element
x2[0,0] # first element of first row
x2[2,-1] # last element of last row

x1[0] = 3.14 # changing single element in array 
x2[0,0] =12 # changing element in multi-dimensional array

# 3) Accessing Subarrays
x= np.arange(10)
x[:6] # first 6 elements
x[6:] # last 6 elements
x[::2] # every other elements
x[1::2] # every other element starting at element 1 


# Multi-dimensional subarrays
x2_sub = x2[:2, :2]
x2_sub[0,0] = 99
x2_sub_copy = x2[:2, :2].copy() # creating a copy 

# 4) Reshaping Arrays
np.arange(25).reshape((5,5))
np.arange(6).reshape((2,3))

# 5) Array Concatenation and Splitting 
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x,y])

z = [100, 322, 323]
print(np.concatenate([x,y,z]))

# Two-dimensional array
grid = np.array([[1,2,3], [4,5,6]])
print(np.concatenate([grid,grid]))

# Using vertical and horizontal stacking
x = np.array([1,2,3])
grid = np.array([[4,5,6], [7,8,9]])

print(np.vstack([x,grid]))

y = np.array([[4],[5]])
print(np.hstack([grid,y]))

# Array Splitting
# np.split, np.hsplit, np.vsplit

x = np.concatenate([np.arange(1,4), [99,99], np.arange(1,4)])
x1,x2,x2= np.split(x, [3,5])
print(x1,x2,x3)

grid = np.arange(16).reshape(4,4)
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])
print(upper)
print(lower)
print(right)
print(left)
