import numpy as np


a = np.arange(10)
arr1 = a[3:8]
a1 = np.array([[1,1], [2,2]])
a2 = np.array([[3,3], [4,4]])

print(np.hstack((a1,a2)))


arr = np.arange(1,25)
print(arr)
arr = arr.reshape(2,12)
print(arr)
arr = np.hsplit(arr, 3)
print(arr)

a = np.arange(1,7).reshape(3,2)
print(a)
print(a[1:3, 0])

import pandas as pd
import os
script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, "results.csv")
data = pd.read_csv("results.csv")
print(data.mean())
print(data.max())
print(data.min())
