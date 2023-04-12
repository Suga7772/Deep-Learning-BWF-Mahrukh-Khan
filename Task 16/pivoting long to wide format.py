import pandas as pd
import numpy as np

# common way of storing multiple time series in databses and csv is in so called long or stacked
# format. Performing some data cleaning and time series wrangling now

data = pd.read_csv('examples/macrodata.csv')
print(data.head(), "\n\n")

# creating multiple time series
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)

data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata[:10], "\n\n")

pivoted = ldata.pivot('date', 'item', 'value')
print(pivoted, "\n\n")

# reshaping two value columns simultaenously
# ldata['value2'] = np.random.randn(len(data))
# print(ldata[:10], "\n\n")

pivoted = ldata.pivot('date', 'item')
print(pivoted, "\n\n")
print(pivoted['value'][:5])

unstacked = ldata.set_index(['date', 'item']).unstack('item')
print(unstacked[:7])



