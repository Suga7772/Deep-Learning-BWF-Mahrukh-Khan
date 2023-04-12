import pandas as pd
import numpy as np

# deducing wether we want to indicate that index should be used as merge key

left1 = pd.DataFrame({'key1': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'val': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print(left1, "\n")
print(right1, "\n")

print(pd.merge(left1, right1, left_on='key1', right_index=True))  # intersect the join keys

# join indexing on multiple hierarchically indexed data

left2 = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
right2 = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])

print("\n\n", left2, "\n\n")
print(right2, "\n\n")

# indicating multiple columns to merge on as a list
print(pd.merge(left2, right2, left_on=['key1', 'key2'], right_index=True), "\n\n")

# handling duplicate index values with outer keyword as opposed to above
print(pd.merge(left2, right2, left_on=['key1', 'key2'], right_index=True, how='outer'), "\n\n")

left3 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
right3 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])

print(left3, "\n")
print(right3, "\n")

# indexing on both sides during merge example for redundant data handling
print(pd.merge(left3, right3, how='outer', left_index=True, right_index=True), "\n\n")

# index on index merges
anothaone = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])

print(anothaone, "\n\n")

print(left3.join([right3, anothaone]), "\n\n")
print(left3.join([right3, anothaone]), how='outer')


