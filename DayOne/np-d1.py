import numpy as np

# Create a 1D NumPy array with values from 0 to 9
a = np.arange(10)
# Slice the array to get values from index 3 up to but not including index 8
arr1 = a[3:8]

# Define two 2x2 arrays for horizontal stacking
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

# Concatenate the arrays side-by-side and print the result
print(np.hstack((a1, a2)))

# Create a 1D array with values from 1 to 24 and print it
arr = np.arange(1, 25)
print(arr)

# Reshape the array into a 2x12 matrix and print it
arr = arr.reshape(2, 12)
print(arr)

# Split the matrix into three equal subarrays along the second axis and print it
arr = np.hsplit(arr, 3)
print(arr)

# Create a 3x2 array and print it
a = np.arange(1, 7).reshape(3, 2)
print(a)

# Print the values from rows 1-2 in the first column
print(a[1:3, 0])

import pandas as pd
import os

# Determine the directory containing this script and construct the CSV file path
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, "results.csv")

# Read the CSV file and print basic summary statistics
data = pd.read_csv(csv_path)
print(data.mean())
print(data.max())
print(data.min())
