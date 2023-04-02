import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6]])
# transposing a matrix with two methods, built-in function and reshape method
print(arr.reshape(2, 3))        # 2 row 3 col
print(arr.reshape(3, 2))        # 3 row 2 col
arr1 = np.arange(6).reshape((2, 3))
print(arr1)
print(arr1.transpose())     # function transpose
print(arr1.T)               # sub alias Func T call

# reversing an array
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
rev_arr2 = np.flip(arr2)        # uno reverse
print(rev_arr2)
# reverse 2dimensional array
arr_2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
rev_arr2d = np.flip(arr_2D)
print(rev_arr2d)
# reverse only rows
rev_arr_rows = np.flip(arr_2D, axis=0)
print(rev_arr_rows)
rev_arr_cols = np.flip(arr_2D, axis=1)
print(rev_arr_cols)
arr_2D[1] = np.flip(arr_2D[1])  # reversing only one row/ col of a 2d matrix
print(arr_2D[1])
arr_2D[:, 1] = np.flip(arr_2D[:, 1])  #column reverse
print(arr_2D)
