import pandas as pd
import numpy as np
# inverse operation of pivot is pandas.melt in Dataframes

# it merges multiple columns into one , producing dataframe longer then the input

df = pd.DataFrame({'key': ['foo', 'soup', 'ballerina'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

print(df, "\n\n")

# key is the group indicator, rest are data values, while using pandas melt we must indicate the group indicator,
# but it's not necessary, unless we want to specify

melted = pd.melt(df, ['key'])
print(melted, "\n\n")

# reshaping it back into original layout
reshape = melted.pivot('key', 'variable', 'value')      # fyi we do get depreciation warning here, better to use keyword next time
print(reshape, "\n\n")

# specifying a subset of columns to use as value columns
print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']), "\n\n")

# using melt without group identifiers
print(pd.melt(df, value_vars=['A', 'B', 'C']), "\n\n")
print(pd.melt(df, value_vars=['key', 'A', 'B']), "\n\n")

