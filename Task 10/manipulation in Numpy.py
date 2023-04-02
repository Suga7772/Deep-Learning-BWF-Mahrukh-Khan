import numpy as np
# adding , removing , sorting elements in an array
arr = np.array([1, 2, 3, 7, 5, 2.4])
print("Before sorting", arr)
print("After sorting", np.sort(arr))

# concatenation of two arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
print("Concatenated array a , b : ", c)

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
z = np.concatenate((x, y), axis=0)
print("Concatenated array of x , y ", z)

# finding shape size of array
arr_e = np.array([[[0, 1, 2, 3],
                   [4, 5, 6, 7]],
                   [[0, 1, 2, 3],
                    [4, 5, 6, 7]],
                  [[0, 1, 2, 3],
                   [4, 5, 6, 7]]])
print("Number of dimensions in array: ", arr_e.ndim)
print("Array size: ", arr_e.size)
print("Array shape: ", arr_e.shape)
