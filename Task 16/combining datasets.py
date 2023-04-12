# hierarchical indexing chapter 8 discussion
import pandas as pd
import numpy as np

# multi indexing example
khajoor = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                                              [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(khajoor, "\n\n")
print(khajoor.index)
print(khajoor['b'], "\n\n")
print(khajoor['b':'c'], "\n\n")     # display b , c indexed corresponding entries

print(khajoor.loc[['b', 'd']], "\n\n")
print(khajoor.loc[:, 2], "\n\n")        # inner level selection
print(khajoor.unstack(), "\n\n")        # rearrange multiindex data in dataframe
print(khajoor.unstack().stack(), "\n\n")        # inverse of unstack

# axis have hierarchical index both can be manipulated
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
print(frame, "\n\n")
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

print(frame['Ohio'], "\n\n")
print(frame.index, "\n\n")

# reordering sorting levels
# identify a row index part of dataframe/series
# lexicography: the activity or occupation of compiling dictionaries
print(frame.swaplevel('key1', 'key2'), "\n\n")              # swap index positions while keeping same values
print(frame.sort_index(level=1), "\n\n")
print(frame.swaplevel(0, 1).sort_index(level=0), "\n\n")    # will sort the first index row in ascending order (a-z | 0-n )

# SUMMARY STATISTICS BY LEVEL
# axis 1 = columns , 0 = rows

print(frame.sum(level='key2'), "\n\n")                           # sum all dedicated 1s, 2s index records
# print(frame.sum(level='color', axis=1))                     # as above is the same as me
print(frame.groupby(level='color', axis=1).sum())


