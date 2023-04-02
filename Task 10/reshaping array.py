import numpy as np
# Reshaping array
a = np.arange(6)
print("Original array: ", a)
b = a.reshape(3,2)  # reshape into 3 row 2 columns
print("Reshaped array: \n", b)
# exploring further parameters with rehsape function
d = np.reshape(a,newshape=(1, 6), order='C')
print(d)

# convert 1d into 2d with newaxis , expand_dim function
# shape function shows row col configuration
e = np.array([1, 2, 3, 4, 5, 6])
print(e.shape)
e2 = e[np.newaxis, :]   # adds another dimension
print(e2.shape)
row_v = e[np.newaxis, :]    # explicitly create one row to make this 1d array into 2d
print(row_v.shape)
col_v = e[:, np.newaxis]    # same as above but for column
print(col_v.shape)
f = np.array([1, 2, 3, 4, 5, 6])
print(f.shape)
# expanding array at specified position , respective of axis
g = np.expand_dims(f, axis=1)
print(f.shape)
h = np.expand_dims(f, axis=0)
print(h.shape)



