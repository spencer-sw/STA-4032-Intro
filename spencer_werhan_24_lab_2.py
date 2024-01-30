# -*- coding: utf-8 -*-
"""Spencer Werhan 24 Lab 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CUF2vLHilQffIoB7u7CeJ6-XbgBXIA89
"""

import numpy as np
import matplotlib.pyplot as plt

numbers= np.array([1,2,2,3,3,3,4,4,4,4])
# Creates an array of numbers

plt.hist(numbers,100);
# Plot a histogram of the array with 100 bins

"""# PRNG"""

x = 3.123 # Initial number

x = x ** 3 # Raise x to the power of 3

x % 1 # Modulus 1 to get the decimal part





# Seed for a PRNG and array initialization
x = 0.12345          # seed value                           # Initial seed value
X = np.zeros(5000,)  # initialize an array of zeros         # Array of zeros with 5000 elements

# Loop to generate pseudorandom numbers

for i in range(X.shape[0]):
    x = 3*x % 1      # update x and store the value in X
    X[i] = x                                                # Store the value in the array X

plt.plot(X, '.')     # plot the values in X

plt.hist(X);
# Plot a histogram of X

# Function to simulate a coin flip
def coin():
    return 2*(np.random.random() > 0.5) - 1

def coin():
    return (np.random.random() > 0.5)

def coin():
    return 2*(np.random.random() > 0.5)

def coin():
    return (np.random.random() > 0.5) - 1

"""The coin() function you've defined is a simple and effective way to simulate a coin flip in Python using the numpy library. Here's an explanation of how it works:

python
Copy code
def coin():
    return 2 * (np.random.random() > 0.5) - 1
def coin(): - This line defines a function named coin. The function doesn't take any arguments.

np.random.random() - This part of the code calls a function from the numpy library to generate a random float between 0 and 1.

> 0.5 - This is a comparison operator. The expression np.random.random() > 0.5 will yield a boolean value: True if the randomly generated number is greater than 0.5, and False if it's less than or equal to 0.5.

2 * (...) - 1 - The boolean value (True or False) is implicitly converted to an integer (1 for True, 0 for False). This integer is then multiplied by 2 and 1 is subtracted. If the random number is greater than 0.5 (True), the result is 2*1 - 1, which equals 1. If the random number is less than or equal to 0.5 (False), the result is 2*0 - 1, which equals -1.

So, this function effectively simulates a coin flip by returning 1 for one outcome (heads) and -1 for the other outcome (tails). It's a neat way to encode a two-outcome event using random numbers.
"""

coin()
# Example usage of the coin function

# Initialize and update a variable using coin function

x = 0
x + coin()

# Another loop for coin flips

x = 0

for i in range(3):
    x = x + coin()

x

# Summing multiple coin flips

x = 0

for i in range(100):
    x = x + coin()

x

# Monte Carlo simulation of coin flips

M = 10000                   # Number of trials
N = 100                     # Number of coin flips per trial

X = np.zeros(M,)            # Array to store results

# Nested loop for the Monte Carlo simulation

for j in range(M):

    x = 0

    for i in range(N):
        x = x + coin()

    X[j] = x

plt.hist(X,100);

# Plotting histogram of the results



"""# Bonus: Explain Pascal's Triangle

Pascal's Triangle is used to find the coefficients in the expansion of binomial expressions

https://www.mathsisfun.com/pascals-triangle.html#:~:text=For%20example%2C%20if%20you%20toss,for%20all%20Tails%20(TTT).
"""

# Pascal's Triangle

P = np.zeros((12,18))                   # Initializing an array for Pascal's triangle

P[0,5]=1                                # Setting the first value

for i in range(1,P.shape[0]):           # Loop to fill in Pascal's triangle

    for j in range(1,P.shape[1]-1):

        P[i,j] = P[i-1,j-1]+P[i-1,j]

# Print a section of Pascal's triangle

print(P[:,5:])

"""# Normal Distribution"""

# Define the parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 0.1  # Standard deviation (sigma) of the distribution

# Generate 1000 data points following a normal distribution with the specified mean and standard deviation
sample_size = 1000
data_points = np.random.normal(mean, std_dev, sample_size)

# Plot the histogram of the data points
bins_number = 30  # Number of bins for the histogram (how many bars want to see)
hist_count, x, ignored = plt.hist(data_points, bins_number, density=True)



x = np.linspace(-5,5,100)   # Array of values from -5 to 5


y = np.exp(x)               # Exponential function of x

np.exp(1)
# Display value of e

plt.plot(x,y)   # Plot y against x

# Plot the probability density function of the normal distribution
normal_dist_curve = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std_dev ** 2))
plt.plot(x, normal_dist_curve, linewidth=2, color='r')

# Set the title and labels for the plot
plt.title('Normal Distribution Visualization')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Display the plot
plt.show()

# Calculating mean, variance, and standard deviation manually

x = np.array([1,2,3,4])

# Sum of elements in x

np.sum(x)

# Number of elements in x

x.shape[0]

# Mean of x

np.sum(x)/x.shape[0]

# Define mean, variance, and standard deviation functions

def mean(x):
    return np.sum(x)/x.shape[0]

# Test the functions

mean(x)

x

x - mean(x)

(x - mean(x))**2

def var(x):
    return mean((x - mean(x))**2)

def std(x):
    return np.sqrt(var(x))

mean(x)

var(x)

std(x)



"""### Uniform Random Numbers

The following codes allow to find a normal distribution from seemingly random numbers
"""

X = np.random.random(50000,)    # Generate an array of 50,000 uniform random numbers between 0 and 1

X

plt.hist(X,100);              # Plot a histogram of the random numbers with 100 bins

np.random.random()      # Generates one random number between 0 and 1

r = np.random.random()  # Generate a single random number between 0 and 1 and stores it in r

r # Calls r to be printed

r = np.random.randint(1,10)   # Generate a random integer between 1 and 10

r # Shows random number generated in previous cell

np.random.randn()

numbers  = np.random.randn(2,4)   # Generate a 2x4 array of random numbers from the standard normal distribution

numbers.shape   # Check the shape of the array

numbers = numbers.reshape(-1)
# Reshape the array to a one-dimensional array

"""# Reshape the array to a one-dimensional array

ChatGPT
Your code snippet performs the following operations using NumPy, a powerful library for numerical computing in Python:

Generate a 2x4 Array of Random Numbers:

python
Copy code
numbers = np.random.randn(2,4)
This line generates a 2-by-4 array (numbers) of random numbers. The random numbers are drawn from the standard normal distribution (mean 0, standard deviation 1).

Check the Shape of the Array:

python
Copy code
numbers.shape
This line checks the shape (dimensions) of the array. For the array numbers, this will return (2, 4), indicating it's a 2x4 array.

Reshape the Array to a One-Dimensional Array:

python
Copy code
numbers = numbers.reshape(-1)
This line reshapes numbers into a one-dimensional array. The -1 in the reshape method is a placeholder that tells NumPy to calculate the appropriate dimension automatically. In this case, the 2x4 array will be flattened into a one-dimensional array of size 8 (since 2*4 = 8).

After executing these lines, numbers will be a one-dimensional array containing the same elements as the original 2x4 array, but laid out in a single row (flattened). This operation does not change the data in the array, only how it's indexed.

User
does reshape always size one dimension down
ChatGPT
The reshape function in NumPy is used to change the shape of an array without changing its data. It doesn't necessarily always reduce the number of dimensions; rather, it reshapes the array to the specified dimensions as long as the total number of elements remains the same. Here are some key points about reshape:

Changing the Number of Dimensions:

Increasing Dimensions: You can use reshape to increase the number of dimensions. For example, a 1D array of size 6 can be reshaped into a 2D array of shape 2x3, or even a 3D array of shape 1x2x3.
Decreasing Dimensions: Similarly, you can reduce the number of dimensions. For example, a 2D array of shape 3x4 can be reshaped into a 1D array of size 12.
Maintaining Dimensions: You can also reshape an array to a different shape with the same number of dimensions, like changing a 2D 3x4 array into a 2D 4x3 array.
Automatic Dimension Calculation:

You can specify -1 for one of the dimensions in the reshape method, which tells NumPy to automatically calculate the size of that dimension based on the size of the other dimensions and the total number of elements in the array.
Requirement for Same Total Size:

The total number of elements in the new shape must match the total number of elements in the original array. For instance, you can't reshape a 2x3 array (6 elements) into a 2x4 array (8 elements) because these shapes do not have the same total number of elements.
Example:
If you have an array arr of shape 2x4 (2 rows, 4 columns), you can reshape it in multiple ways:

To a 1D array (flattening): arr.reshape(-1) or arr.reshape(8).
To a different 2D array: arr.reshape(4, 2).
To a 3D array: arr.reshape(2, 2, 2).
In summary, reshape is a versatile function that can be used to alter the shape of an array in various ways, as long as the total number of elements remains constant.
"""

numbers.shape   # Check the new shape of the array

numbers= np.array([1,2,2,3,3,3,4,4,4,4])    # Create a specific numpy array

plt.hist(numbers,100);
# Plot a histogram of the array with 100 bins

numbers = np.random.randn(100000,)
plt.hist(numbers,100);

# Generate 100,000 random numbers from the standard normal distribution and plot a histogram

numbers = np.random.rand(1000000,)
plt.hist(numbers,100);

# Generate 1,000,000 uniform random numbers between 0 and 1 and plot a histogram

# Set a seed for the random number generator and generate random data

np.random.seed(12345)
data = np.random.randn(2, 100)


# Create subplots to visualize the data in different forms

plt.figure(1, figsize=(9, 9))

plt.subplot(2,2,1)
plt.hist(data[0])

plt.subplot(2,2,2)
plt.scatter(data[0], data[1])

plt.subplot(2,2,3)
plt.plot(data[0], data[1],'-')

plt.subplot(2,2,4)
plt.hist2d(data[0], data[1])

plt.show()

"""Normal Dist Data"""

# Generate 10,000 random numbers from a normal distribution (scaled by 10) and plot a histogram

x = 10*np.random.randn(10000)

plt.hist(x);

# Generate 1,000 uniform random numbers between 0 and 1 and plot a histogram

x = np.random.rand(1000,)

plt.hist(x);



# Set mean and standard deviation for the normal distribution

mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution

# Generate random numbers from the normal distribution and plot a histogram

x = mu + sigma * np.random.randn(10000)

n,bins,patches = plt.hist(x,bins=100)

bins

# Plot the probability density function over the histogram

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(y)

num_bins = 50
n,bins,patches = plt.hist(x, num_bins, density=1)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(bins,y)



x

"""Define functions to calculate mean, variance, standard deviation, median, mode, and range"""

def mean(x):
    return np.sum(x)/x.shape[0]

def var(x):
    return mean((x - mean(x))**2)

def std(x):
    return np.sqrt(var(x))

def median(x):
    n = len(x)
    sorted_x = np.sort(x)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_x[mid - 1] + sorted_x[mid]) / 2
    else:
        return sorted_x[mid]

def mode(x):
    values, counts = np.unique(x, return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]

def range(x):
    return np.max(x) - np.min(x)

# Test the functions with an example array

data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6])

# Testing the functions
mean_value = mean(data)
var_value = var(data)
std_value = std(data)
median_value = median(data)
mode_value = mode(data)
range_value = range(data)

mean_value, var_value, std_value, median_value, mode_value, range_value



"""# Homework



"""



"""# Pi from Random Numbers

graph 2x2 square centered on origin
area is 4
if drew circle in middle of square area is pi*r^2
hit inside cirlce
miss outside circle
pi/4=hit/total
"""

N = 10000 # back off to reasonable number like 10

points = -1 + 2*np.random.random((N,2))

points # do not run with 10000

plt.plot(points[:,0],points[:,1],'.')

plt.gca().set_aspect(1)

inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1
outside_circle = points[:,0]**2 + points[:,1]**2  > 1

plt.plot(points[inside_circle,0],points[inside_circle,1],'g.')
plt.plot(points[outside_circle,0],points[outside_circle,1],'r.')


plt.gca().set_aspect(1)

np.sum(inside_circle),np.sum(outside_circle)

total_area = 4

fraction_inside = np.sum(inside_circle)/N

fraction_inside*total_area

N = 100000000
points = -1 + 2*np.random.random((N,2))
inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1
fraction_inside = np.sum(inside_circle)/N
fraction_inside*4

"""# Complete Code for Estimating π using Monte Carlo Simulation"""

# Number of random points to generate
num_points = 100000

# Generating random points
x_points = np.random.uniform(-1, 1, num_points)
y_points = np.random.uniform(-1, 1, num_points)

# Calculating the number of points inside the quarter circle
points_inside = np.sqrt(x_points**2 + y_points**2) <= 1
num_inside = np.sum(points_inside)

# Estimating π
pi_estimate = 4 * num_inside / num_points

# Plotting the points and the quarter circle
plt.figure(figsize=(6, 6))
plt.scatter(x_points[points_inside], y_points[points_inside], color='green', label='Inside')
plt.scatter(x_points[~points_inside], y_points[~points_inside], color='red', label='Outside')
circle = plt.Circle((0, 0), 1, color='blue', fill=False)
plt.gca().add_artist(circle)
plt.title('Estimating π using Monte Carlo Simulation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal')
plt.show()

pi_estimate





"""# e from Random Numbers"""

X = np.random.random((1000000,10))

Y = np.cumsum(X,1)

Z = np.argmax(Y > 1,1) + 1

np.mean(Z)

np.mean(np.argmax(np.cumsum(np.random.random((10000000,10)),1) > 1,1) + 1)

np.exp(1)





"""# Further Reading:

### Quantum Random Numbers API

https://aws.amazon.com/marketplace/pp/prodview-246kyrfjo3bag
"""


