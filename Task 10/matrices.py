import numpy as n
d = n.array([[1, 2], [3, 4]])
o = n.array([[1, 1], [1, 1]])
print(d)
print(d[[0, 1]])
print(d[1:3])
print(d[0:2, 0])
print(d.max())  # 4
print(d.min())  # 1
print(d.sum())  # 10
print(d.max(axis=0))    # row
print(d.max(axis=1))    # col
# arithmetic operations on matrices
print(d + o)
o1 = n.array([[1, 2], [3, 4], [5, 6]])
o2 = n.array([[1, 1]])
print(o1 + o2)

