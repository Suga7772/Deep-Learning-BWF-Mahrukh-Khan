import pandas as pd
import numpy as np

fram = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                     'c': ['one', 'one', 'one', 'two', 'two',
                           'two', 'two'],
                     'd': [0, 1, 2, 0, 1, 2, 3]})
print(fram, "\n\n")
fram1 = fram.set_index(['c', 'd'])  # creating new dataframe using one or more of fram cols as index
print(fram1, "\n\n")

print(fram.set_index(['c', 'd'], drop=False), "\n\n")   # columns removed by default "droppped" but you can revoke that using
# drop=false

# reset _index moves the heirarchical index levels into colums
print(fram1.reset_index())

