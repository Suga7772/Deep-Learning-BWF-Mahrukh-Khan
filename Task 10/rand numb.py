import numpy as np
import random
# simplest way to gen random numbers
rng = np.random.default_rng(0)

print(rng.random(3))  # will print an array with 3 random eleents
print(rng.random((3, 2)))     # with gen random number arrays you can set endpoints for inclusiveity
print(rng.integers(5, size=(2, 4)))
# getting unique item and counts

a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
uniq_val = np.unique(a) # will remove redundant recurring elements
print(uniq_val)
# will print index of unique elements
uniq_valu, ind_list = np.unique(a, return_index=True)
print(ind_list)
print(uniq_valu)
uniq_val, occur_count = np.unique(a, return_index=True)
print(occur_count)      # occurences of unique elements in array a
# example of unique function with 2 dimensional arrays
aTwoDim = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
uniq_val = np.unique(aTwoDim)       # calculating unique with 2d array
print(uniq_val)
uniq_rows = np.unique(aTwoDim, axis=0)  # unique values row wise
print(uniq_rows)
