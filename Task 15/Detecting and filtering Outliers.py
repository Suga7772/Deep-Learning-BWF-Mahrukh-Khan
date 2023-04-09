import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[2]
print(col[np.abs(col) > 3], "\n\n") # values in one of the columns exceeding 3 in absolute values

print(data[(np.abs(data) > 3).any(1)], "\n\n")      # select rows having value exceeding 3 or -3

# capping the criteria in interval 3 to -3
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe(), "\n\n")

# sign (data) bases in interval 1 to -1 , on criteria of
# wether they are positive or negative

print(np.sign(data).head())


