import numpy as np

x = np.array([2, 4, 5, 6, 1, 1])
y = np.array([5, 6, 7, 1, 2, 4])

print(np.intersect1d(x, y))     # common elements in x, y
print(np.union1d(x, y))         # sorted union of elements
print(np.in1d(x, y))            # boolean array indicating if each element in other array
print(np.setdiff1d(x, y))       # set difference of elements in x that are not in y
print(np.setxor1d(x, y))        # set symmetric difference

