import numpy as np

data = np.array([[2, 3, 4, 6, 12], [1, -9, 5.6, 3, 11]])
data2 = np.array([[0., 4, 1, 3, 5], [-13, 7, 2, 12, 13]])

print(data > data2)
print(data ** 2)
print(data + data2)
print(data - data2)
print(data * data2)
print(data2 / data)

print(1 / data)