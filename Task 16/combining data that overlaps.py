import numpy as np
import pandas as pd
from numpy import nan as NA

# we may have datasets whose indexes overlap fully , so to handle them
# we use numpy where function that computes array-equivalent of if-else operation

a = pd.Series([NA, 2.5, NA, 3.5, 4.5, NA],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b[-1] = NA
print(a, "\n\n")
print(b, "\n\n")

# following both lines of code are equivalent to each other, patching missing data in calling object with data from object passed
print(np.where(pd.isnull(a), b, a), "\n\n")
print(b[:-2].combine_first(a[2:]), "\n\n")

df1 = pd.DataFrame({'a': [1., NA, 5., NA], 'b': [NA, 2., NA, 6.], 'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., NA, 3., 7.], 'b': [NA, 3., 4., 6., 8.]})

print(df1, "\n\n")
print(df2, "\n\n")

print(df1.combine_first(df2), "\n\n")
