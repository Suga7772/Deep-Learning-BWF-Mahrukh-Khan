import numpy as np
import pandas as pd
from numpy import nan as NA

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA

print("Original dirty data \n", df)

print("Filled data: \n", df.fillna(0))

# filling null entries with dictionary

print(df.fillna({1: 7.9, 2: 0.69}))

# analysing return type of fillna function invoked on dataframe
_ = df.fillna(0, inplace=True)
print(df)

# testing out another interpolation method with fillna

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print("New df before interpolation with fillna:\n", df)
print("New df after interpolation with fillna:\n", df.fillna(method='ffill'))
print("New df after interpolation with fillna and limit 2:\n", df.fillna(method='ffill', limit=2))\

# doing cool things with fillna , e.g. passing mean

datemesenpai = pd.Series([1, NA, 3.5, NA, 7])
print(datemesenpai.fillna(datemesenpai.mean()))
