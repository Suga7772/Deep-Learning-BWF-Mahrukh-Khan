import pandas as pd
import numpy as np

# another type of data combination
# synonyms : concatenation, binding , stacking
# implemented using numpys concatenate function

arr = np.arange(12).reshape((3, 4))
print(arr, "\n\n")
print(np.concatenate([arr, arr], axis=1), "\n\n")

# working with pandas, initial example for series with no overlap concat
# by default concat works on axis 0 (row), have to pas axis=1 (will create dataframe , cols )

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

print(pd.concat([s1, s2, s3]), "\n\n")
print(pd.concat([s1, s2, s3], axis=1), "\n\n")  # no overlap, alotta nan values

s4 = pd.concat([s1, s3])
print(s4, "\n\n")

print(pd.concat([s1, s4], axis=1), "\n\n")
print(pd.concat([s1, s4], axis=1, join='inner'), "\n\n")

# specifying join axis :  following reates argument issue for join axes
# print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]), "\n\n")

# we cannot identify the concatenated pieces, so to identify them we can introduce indexing by keys argument
res = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])
print(res, "\n\n")
print(res.unstack(), "\n\n")

# defining the axis for col (1) makes the keys as dataframe column headers
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']), "\n\n")

# same logic applies to data frame objects, quick example below
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])

print(pd.concat([df1, df2], axis=1, keys=['lvl1', 'lvl0']), "\n\n")

# passing dict of objects will make the dict keys used as keys
print(pd.concat({'level1': df1, 'level2': df2}, axis=1), "\n\n")

# handling dataframe data where rows contains no irrelevant data

df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

print(df1, "\n\n")
print(df2, "\n\n")
print("Concatenating df1 df2 : \n\n", pd.concat([df1, df2], ignore_index=True))
