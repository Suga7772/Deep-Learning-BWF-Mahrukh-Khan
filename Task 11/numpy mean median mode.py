# diving into statistic side of things
import numpy as np
import scipy.stats as sp
arr = np.random.randn(5, 4)
a2 = np.array([[2, 13, -5, 9], [6, -79, 1, 0]])
print(arr)

# MEAN
print(np.mean(arr))
# arr.mean(0) mean in row
print(np.mean(arr, axis=0))
# arr.mean(1) mean in col
print(np.mean(arr, axis=1))

# MEDIAN
print(np.median(arr))

# MODE NUMPY DON'T GOT , lets go it using scipy package
keepdims = True
print(sp.mode(a2))
print(arr.std())        # standard deviation

# quartiles
print(a2[int(0.05* len(a2))])       # 5% non numpy way
print(np.quantile(a2, 0.45))        # 45 % numpy way
print(np.quantile(a2, 0.75))        # 75 % numpy way

# ranks
print("Array rank: ", np.linalg.matrix_rank(a2))


print(arr.min())
print(arr.max())

arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

print(arr1)
print(arr.cumsum(axis=0))       # does not aggregate, accumulation sum
print(arr.cumsum(axis=1))
print(arr.cumprod(axis=1))
