import numpy as np
# broadcasting the arithmetic workings between arrays of different arrays

# simplest applicaton : combining a scaler value with an array

a1 = np.arange(5)       # array 0, 1, 2, 3, 4
print(a1)
print(a1 * 4)   # WE SAY THAT scalar value 4 has been broadcast to all other elements in a1 array

# demeaning , rollback the mean operation on an array elements
a2 = np.random.randn(4, 3)
a2.mean(0)
print(a2)

demean = a2 - a2.mean(0)
print(demean)

demean.mean(0)
print(demean)

# # broadcasting tips and common errors:
# broadcast dimensions when performing arithmetic operations is that
# the other array must be 1 in the smaller array. (4,3) operations with (4)
# will be false but correction is (4,3) with (4,1)

# addition
x = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
y = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
print(x+y)


# special new axis by index method , np.newaxis with full slices
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :]
print(arr_3d)
arr_1d = np.random.normal(size=3)
arr_1d[:, np.newaxis]
print(arr_1d)
arr_1d[np.newaxis, :]
print(arr_1d)

# setting valus by broadcasting (arrays)

a2 = np.zeros((4, 3))
a2[:] = 5
print(a2)
col = np.array([1.28, -0.420, 0.44, 1.6])
a2[:] = col[:, np.newaxis]
print(a2)
a2[:2] = [[-1.37], [0.509]]
print(a2)