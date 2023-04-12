# pandas can store multiple amounts of data , many of which we need to assess together , in a combined form
# data merge/ combine methods include merge, concat, combine_first
import pandas as pd

# DATABASE STYLE DATA FRAME JOINS

df1 = pd.DataFrame({'key': ['b', 'a', 'b', 'c', 'c', 'a', 'a'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['b', 'b', 'a'],
                    'data2': range(3)})

print(df1, "\n")
print(df2, "\n")

# database joins can go about on join concept
# many to one join ,similar attritbutes matched are place in the combined dataframe
# if we don't specify which column to join on, merge uses overlapping columns names as keys
# but good to explicitly tell tho
print("Merge two dataframes: \n", pd.merge(df1, df2), "\n")

# explicit join col specified
print(pd.merge(df1, df2, on='key'), "\n")

# we can specify column names in the case of distinct names in each obj
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

# c and d values are missing, rightfully as to showcase nature of inner joins, result is common set found in both tables
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'), "\n\n")

print("Many to many merges Example: \n\n")

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})

print("D1: ", df1, "\n")
print("D2: ", df2, "\n")

print(pd.merge(df1, df2, on='key', how='left'), "\n\n")  # cartesian product of rows

print(pd.merge(df1, df2, how='inner'), "\n")

# merging multiple keys

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

print(pd.merge(left, right, on=['key1', 'key2'], how='outer'), "\n\n")


# treating overlapping column names is handled by suffix alottment
# conventional merge
print(pd.merge(left, right, on='key1'), "\n\n")
# handled auto merge,
print(pd.merge(left, right, on='key1', suffixes=('left', 'right')), "\n\n")
