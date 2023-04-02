import numpy as np
# arithmetic operations
d = np.array([1, 2])
one = np.ones(2, dtype=int)
print(one)  # [1, 1]
print(d + one)  # [2, 3]
print(d - one)  # [0, 1]
print(d * one)  # [1, 4]
print(d / d)  # [1, 1]
# sum of arrays
a = np.array([1, 2, 3, 4])
print(a.sum())
b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))    #sum rows
print(b.sum(axis=1))    #sum columns
# BROADCASTING
d1 = np.array([1.0, 2.0])
print(d1 * 1.6)     # [1.6, 3.2]
print(d1.max())    # 1
print(d1.min())    # 3
print(d1.sum())    # 6
a1 = np.array([[0.45053314, 0.1729677, 0.3427558, 0.5510652],
               [0.5467315, 0.05093587, 0.40067661, 0.55645993],
               [0.12697628, 0.82485413, 0.26590556, 0.56917101]])
print(a1.sum())
print(a1.min())
print(a1.min(axis=0))   # find min in column
