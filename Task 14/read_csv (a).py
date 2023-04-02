# to read a csv (comma separated value) file, one must create one!
import pandas as pd

# to red the csv file without the comma and more formatted better
# appearance, we can assign it via pandas and read it
dp = pd.read_csv('examples/ex1.csv')
print(dp)

print("\n\n", pd.read_csv('examples/ex2.csv', header=None))
print("\n\n", pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message']))

# we can specify index columns

n = ['a', 'b', 'c', 'd', 'msg']
print("\n\n", pd.read_csv('examples/ex2.csv', names=n, index_col='msg'))

parsed = pd.read_csv('examples/csv_mindex.csv', index_col=['key1', 'key2'])
print("\n\n", parsed)

result = pd.read_csv('examples/ex5.csv')
print("\n\n", result)

print("\n\n", pd.isnull(result))

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}

print("\n\n", pd.read_csv('examples/ex5.csv', na_values=sentinels))

# in case of massive datasets , we can use limited rows for showing
print("\n\n", pd.read_csv('examples/csv_mindex.csv', nrows=5))

data = pd.read_csv('examples/ex5.csv')
print("\n\n", data)
print("\n\n", data.to_csv())