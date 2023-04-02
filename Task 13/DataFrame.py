from data import pop, data, np, obj, obj2, pd, Series, DataFrame

# dataframe represents a rectangular table of data and contains
# collection of columns, each with different data types
# has a both row and column index, almost like a dictionary of series all sharing same index

frame = pd.DataFrame(data)
print(frame)

# in large dataframes, head method is good as it shows only first five rows
print(frame.head())

# order arrangement by defining column placement
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

# in frame 2, debt is not defined in data Dataframe so it'll be nill
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])

print(frame2)
print(frame2.columns)

# can retrieve cols in dataframe in dictionary like notation
print(frame2['state'])

# rows can be retrieved by position or name with 'loc' attribute
print(frame2.loc['three'])

# modification via assignment
frame2['debt'] = 1.65
print(frame2)
frame2['debt'] = np.arange(6.0)

# when we assign data to a column that doesn't exist, that column will be created
frame2['eastern'] = frame2.state == 'Alabama'
print(frame2)

# deletion of column
del frame2['eastern']
print(frame2.columns)

# interpretation of nested dictionary in panda :
frame3 = pd.DataFrame(pop)
print(frame3)

# transpose
print(frame3.T)

# in dictionaries , inner dict keys are combined and sorted to form index in result
# that won't be done if explicit index are specified
print(pd.DataFrame(pop, index=[2001, 2005, 2002]))

# dictionary of series
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

# passing dataframe constructor
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)

# values return a 2d array for dataframe
print(frame3.values)

# if Dataframe col of different data type then values of array Object will be chosen to accomadate
print(frame2.values)



