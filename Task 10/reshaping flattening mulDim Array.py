import numpy as np
# covers flatten and ravel functions
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 14]])
# flatten converts 2d array into 1d array
print(x.flatten())          # temporary change
a1 = x.flatten()
a1[0] = 99
print("Original array : ", x)        # org array
print("Flatten : ", a1)
# in ravel changes affect parent array
a2 = x.ravel()
a2[0] = 98
print("Ravel: ", a2)
