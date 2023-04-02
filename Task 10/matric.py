import numpy as np
import random
arr = np.array([[1, 2], [3, 4]])        # creating an array
print(arr.max(axis=0))  # row
print(arr.max(axis=1))  # column

# arithmetic operations b/w two matrices
d0 = np.array([[1, 2], [3, 4]])
d1 = np.array([[1, 1], [1, 1]])
print(d0 + d1)

# perfroming operations from different array dimensions
d2 = np.array([[1, 2], [3, 4], [5, 6]])
one_r = np.array([[1, 1]])      # matrix with one row
print(d2 + one_r)
print(np.ones((4, 3, 2)))       # will print n dimensional arrays, last axis is loops over fastest while firs axis is lowest
print(np.ones(3))      # print one row array with 1s in each of 3 element
print(np.zeros(3))
print(np.ones((3, 2)))
print(np.zeros((3, 2)))






