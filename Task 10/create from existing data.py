import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a1 = a[3:8]     # grabbing section of a 3 - 8 index
print(a1)
# stacking array
a2 = np.array([[1, 1], [2, 2]])
a3 = np.array([[3, 3], [4, 4]])
print(a2)
print(a3)
# vertically stacking
print(np.vstack((a2, a3)))
# horizontally
print(np.hstack((a2, a3)))
# splitting arrays
x = np.arange(1, 25).reshape(2, 12)
print(x)
print(np.hsplit(x, 3))
print(np.hsplit(x, (3, 4)))

a4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a4[0, :]
# slicing techniques and further modifying an arr a4 in b
print(b)
print(b[0])
print(a4)
b1 = a.copy()   # make complete copy of a in b1
print(b1)
