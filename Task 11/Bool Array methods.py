import numpy as np

a1 = np.random.randn(100)
print((a1 > 0).sum())

bool1 = np.array([True, False, False, True])
print(bool1.any())       # true if any element is true
print(bool1.all())       # true is all element true

# sorting
a2 = np.array([[2, 13, -5, 9], [6, -79, 1, 0]])
print(a2)
a2.sort()   # sorts elements in ascending order respective to rows
print(a2)


# unique
dancers = np.array(['ballerina', 'micheal', 'vix', 'suga', 'micheal', 'vix'])
print(np.unique(dancers))

ints = np.array([3, 3, 3, 4, 54, 51, 2, 1, 4, 4])
print(np.unique(ints))

print(sorted(set(dancers)))
