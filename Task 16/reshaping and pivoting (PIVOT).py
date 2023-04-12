import numpy as np
import pandas as pd

# discussing and understanding the various basic operations for rearranging tabular data

# reshaping with hierarchical indexing

# two primary functions stack ( rotates from cols in the data to rows)
# unstack ( pivots from rows into the columns )

date = pd.DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))

print(date, "\n\n")
res = date.stack()
print(res, "\n\n")
# rearranging back with stack
print(res.unstack(), "\n")
# passing specific levels to be rearranged

print(res.unstack(0), "\n")
print(res.unstack('state'), "\n")

# missing data will be found if stacking values not cordinated in each of the sub groups
s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
date2 = pd.concat([s1, s2], keys=['one', 'two'])

print(date2, "\n\n")
print(date2.unstack(), "\n\n")
# stacking filters missing date out by default
print(date2.unstack().stack(), "\n\n")
print(date2.unstack().stack(dropna=False))  # to manually revert default missing data handling

df = pd.DataFrame({'left': res, 'right': res + 5},
                  columns=pd.Index(['left', 'right'], name='side'))

print(df, "\n\n")
print(df.unstack('state'), "\n\n")
print(df.unstack('state').stack('side'), "\n\n")

