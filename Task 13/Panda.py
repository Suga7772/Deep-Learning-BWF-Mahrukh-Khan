# pandas is a tool for data manipulation, data cleaning and swift analysis
# most popular and chimed data structures of pandas
from data import obj, obj2, pd

print(obj)
print(obj.values)
print(obj.index)

# explicitly changing default index numeration (0 onwards) with alphabets
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)

print(obj2.index)

# printing element respective to index
print(obj2['a'])
print(obj2['d'])
print(obj2[['c', 'a', 'd']])        # interpreted as list of indices

