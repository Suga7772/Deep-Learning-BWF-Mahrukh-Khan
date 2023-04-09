import pandas as pd
import numpy as np

data = pd.Series([1., -999., 2., -999., -1000., 3.])

print(data, "\n")

print(data.replace(-999, np.nan), "\n")     # replacing single value
print(data.replace([-999, 1000]), "\n")      # replacing multiple values in the form of a list

# passing substitutes for specific entries to replace
print(data.replace([-999, 1000], [np.nan, 0]))

# can also pass with dictionarys
print(data.replace({-999: 0, 1000: np.nan }))
