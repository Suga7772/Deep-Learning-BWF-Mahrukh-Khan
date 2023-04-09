import pandas as pd
import numpy as np
from numpy import nan as NA

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

# returning duplicate entries answer

print("\n\n", data.duplicated())
print("\n\n", data.drop_duplicates())

# filter based on sppcific columns
data['v1'] = range(7)
print("\n\n", data.drop_duplicates(['k1']))

# default is first two columns ,to explicitly call last col use keep last parameter

print("\n\n", data.drop_duplicates(['k1', 'k2'], keep='last'))

