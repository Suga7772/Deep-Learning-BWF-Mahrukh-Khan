# handling missing data
import pandas as pd
import numpy as np
from numpy import nan as NA
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'zucciihni', 'artichoke'])

print(string_data)

# highlight null entry , isnull function corresponds to boolean outputs for empty/non-empty entries
print(string_data.isnull())

string_data[0] = None
print(string_data.isnull())

dateme = pd.Series(['1', NA, 89990.3, "Banananas", 'Ballerina'])

print(dateme.dropna)
# equivalent to dateme[dateme.notnull()]

# worrking with dataframes

datemepls = pd.DataFrame([[1.0, 6.5, 79], [1.4, NA, NA], [NA, NA, NA], [NA, 6.9, 1.3]])

print("Uncleaned data: \n ", datemepls)     # dirty data
print("cleaned data: \n", datemepls.dropna())
print("cleaned data: \n", datemepls.dropna())
print(datemepls.dropna(how="all"))      # will only remove data with all rows as NA
datemepls[4] = NA
print(datemepls)
print(datemepls.dropna(axis=1, how='all'))

# filtering data concerning with rows and colunms , with thresh arguments

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())

print(df.dropna(thresh=2))
