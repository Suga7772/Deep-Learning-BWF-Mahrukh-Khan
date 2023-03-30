# numPy short for numerical python , provides data structures, algo and library glue
import numpy as np # importing numpy library with an alias
import time

a = np.array([1, 2, 3, 4, 5, 6, 7])     # one dimensional array
print(a)
print(a+a)
print(a-a)
print(a*a)
print(a/a)

my_arr = np.random.randn(2, 3)      # two-dimensional array , matrix
print(my_arr)

# arithmetic operations
print(my_arr * 10)
print(my_arr + my_arr)
print(my_arr - my_arr)
print(my_arr / 2)
print(my_arr ** 3)

# getting data configuration

print(my_arr.shape)   # (2, 3)
print(a.shape)  # 7 elem in 1 row

# getting data type in each array

print(my_arr.dtype)
print(a.shape.dtype)

# printing zero array
print(np.zeros(10))     # 10 zeroes
