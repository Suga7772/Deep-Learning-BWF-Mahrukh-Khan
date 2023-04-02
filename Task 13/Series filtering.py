from data import obj, obj2, pd, np, Series

print(obj2[obj2 > 0])

print(obj2 * 2)

print(np.exp(obj2))


# series can be thought of s a fixed length, ordered dictionary with
# mapping of index values to data values

print('b' in obj2)
print('e' in obj2)

# creating series via dictionary

sdata = {'Ohio': 3500, 'Texas': 71000, 'Alabama': 16000, 'Ohio': 9900}
obj3 = pd.Series(sdata)

print(obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(states)
print(obj4)

print(pd.isnull(obj4))
print(obj4.isnull())        # same as above

# Series automatically aligns by index label in artihmetic operations
print(obj3)
print(obj4)

print(obj3 + obj3)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

print(obj)
# changing index in obj attribute
obj.index = ['Bob', 'Steve', 'MyNameisJeff', 'Ryan']
print(obj)