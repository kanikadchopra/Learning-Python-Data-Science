import numpy as np
import matplotlib.pyplot as plt

## Topics Covered:
# 1) Introducing UFuncs
# 2) Exploring NumPy's UFuncs: Array Arithmetic, Absolute Value (with complex),
# trigonometric functions, exponents and logarithms, specialized UFuncs: 
# 3) Advanced uFunc features - specifying output, aggregates, outer products
# 4) Aggregations - Summing, min, max, multidimensional aggregates, 
# 5) Broadcasting: rules of broadcasting, centering an array, plotting a
# two-dimensional function


# 1) Introducing UFuncs 
# reciprocal for array

np.random.seed(0)
## This function takes an array of values, and divides each by 2 and then returns
## an output array that has all the values divided by 2
def div_by_2(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = values[i]/2
    return output

values= np.random.randint(1,10,size=5)
div_by_2(values)
big_array = np.random.randint(1, 100, size=100000)

## 2) Exploring NumPy's UFuncs

# Array arithmetic
x= np.arange(5)
print("Original array:",x)
print("Add 10:",x+10)
print("Subtract 10:", x-10)
print("Multiply by 4:", x*4)
print("Divide by 3:", x/3)
print("Integer division by 2:", x//2)
print("Cubed:", x**3)
print("Squared:", x**2)
print("Square root:", x**(1/2))
print("Negation:",-x)
print("Mod by 2:", x%2)
print("Set of operatons:", -(3*x +1)**2)
print('/n')

# Absolute value
x1 = np.arange(-5, 6)
print("Before abs list:", x1)
print("Absolute value:", abs(x1))

# Complex numbers
x2 = np.array([3-3j, 2-3j, 2+0j, 0+5j, 0+0j])
print("Complex array:", x2)
print("Magnitude of complex:", abs(x2))
print('/n')

# Trigonometric Functions 
thetha = np.linspace(0, np.pi, 3)
print("thetha:", thetha)
print("sin", np.sin(thetha))
print("cos:", np.cos(thetha))
print("tan:", np.tan(thetha))
reverselst= [1,0,-1]
print("List for inverse trig:", reverselst)
print("arcsin:", np.arcsin(reverselst))
print("arccos:", np.arccos(reverselst))
print("arctan:", np.arctan(reverselst))

# Exponents and Logarithms
print('\n')
exp =[1,2,3]
print(np.exp(exp))
print(np.exp2(exp))
print(np.power(3,exp))

logs = [1,2,4,10]

# Special UFuncs
from scipy import special
y = [1,5,10]

# Error function# Gamma functions (generalized factorials) and related functions
print(y)
print(special.gamma(y))
print(special.gammaln(y))
print(special.beta(y,2))

# Error function (integral of Gaussian), its complement and its inverse
z = np.array([0, 0.3, 0.7, 1.0])
print(z)
print(special.erf(z))
print(special.erfc(z))
print(special.erfinv(z))

# Refer to a project with combinations and permutations for more practice with special 

# 3) Advanced UFuncs
# Specifying output 
x = np.arange(10)
y = np.empty(10)
np.divide(x, 2, out=y)

y = np.zeros(20)
np.multiply(x, 2, out=y[::2])

# Aggregates
x = np.arange(5,15)
np.add.reduce(x) # the sum
np.multiply.reduce(x) # the product
y = np.arange(5)
np.multiply.reduce(y) # 5!
np.multiply.accumulate(y) # All the factorials 

# Outer Products
x = np.arange(1,10)
mult_table = np.multiply.outer(x,x) # Create a multiplication table
print('\n')
print("Multiplication table:")
print(mult_table)

# 4) Aggregations
# Summing an array
L = np.random.random(50)
np.sum(L) # faster than using the sum function

# Min, Max
mini = np.min(L)
maxi = np.max(L)

# Multidimensional aggregates
M = np.random.random((5,4))
sums = M.sum()
min_col = M.min(axis=0)
min_row = M.min(axis=1)

max_col = M.max(axis=0)
max_row = M.max(axis=1)

# 5) Broadcasting 
a = np.array([0,1,2])
b = np.array([5,5,5,])
print("a+b:", a+b)
print("a+5:", a+5) 

# One-dimensional array to two-dimensional array
M = np.ones((3,3))
print("M+a:", M+a)
print("M+b:", M+b)

# Broacasting of both arrays
a = np.arange(4)
b = np.arange(4)[:, np.newaxis]
print("Broadcasting two arrays:", a+b)

# Testing out rules of broadcasting:
# Ex 1: Two-dimensional array to a one-dimensional array
M = np.ones((4,5))
a = np.arange(5)

print("M shape:", M.shape)
print("a shape:", a.shape)

# Predicted shape is a (4,5)
print("M+a: is it a (4,5)?:", M+a)

# Ex 2: Both arrays need to be broadcasted
a = np.arange(3).reshape((3,1))
b = np.arange(3)

# Predicted shape is a (3,3)
print("a+b: is it (3,3)?:", a+b)

# Ex 3: Not compatible arrays
N = np.ones((3,2))
c = np.arange(3)

# This creates an array unless we reshape c explicitly
c_t = c[:, np.newaxis]
print("This works after changing c's shape:", N+c_t)

# Centering an array 
X = np.random.random((10,3))
Xmean = X.mean(0)
print("The mean is:", Xmean)
X_centered = X - Xmean

# Check that this is done correctly
print("Close to zero:", X_centered.mean(0))

# Self-created example: Let's say we have data we observed for 5 stores the sales
# of apples, bananas, oranges. We want to know the mean of each of the fruits 
# from all the stores. The data is stored in fruit_sales, we want a centered array.
fruit_sales = np.array([[42,34, 69], [32, 46,74], [23,24, 57], [17, 46, 34], [36, 23, 73]])
print("The mean sales are:", fruit_sales.mean(0))
print("The mean apple sales are:", fruit_sales.mean(0)[0])
print("The mean bananas sales are:", fruit_sales.mean(0)[1])
print("The mean oranges sales are:", fruit_sales.mean(0)[2])
fruit_sales_centered = fruit_sales - fruit_sales.mean(0)

# Plotting a two-dimensional function
x = np.linspace(0,5,50)
y = np.linspace(0,5,50)[:,np.newaxis]
z = np.sin(x) ** 10 + np.cos(10+y*x)*np.cos(x)

# Graphing a density and contour plot
plt.imshow(z, origin='lower', extent=[0,5,0,5], cmap='viridis')
plt.colorbar();
