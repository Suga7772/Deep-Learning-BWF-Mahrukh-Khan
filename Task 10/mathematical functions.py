import numpy as np

predictions = np.array([1, 1, 1])
labels = np.array([1, 2, 3])
n = 3
error = (1/n) * np.sum(np.square((predictions - labels)))
print(error)        # 1.6666 ans

# loading and saving projects
# saving an array
a = np.array([1, 2, 3, 4, 5, 6])
print (a)
np.save('filename1', a)
# loading npy
b = np.load('filename1.npy')
# checking array
print(b)
# saving csv file
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
np.savetxt('new_file_csv', csv_arr)
# loading saved csv file
print(np.loadtxt('new_file_csv'))
