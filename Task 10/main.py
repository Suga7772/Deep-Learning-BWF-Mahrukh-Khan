import numpy as np
# Numpy used for the array procedure , referred as dtype

a = np.array([1,2,3,4,5,6])
print(a[0])

# following z  b arrays will print the same
z = np.zeros(2)
print(z)

b = np.empty(2)
print(b)

# printing an array with range of elements
c = np.arange(4)
print(c)        # [0 , 1, 2, 3]

d = np.arange(2,9,2)  # (first number ,last number , increment size)
print(d)

e = np.linspace(0,10, num=5)    # defining an array with linear space
print(e)

# specifying data type , in this case, array of ones
x = np.ones(2,dtype = np.int64)
print(x)
