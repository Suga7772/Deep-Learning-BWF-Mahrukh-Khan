import numpy as np
data = np.array([1, 2, 3])
# slicing and indexing
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[a < 5])
fiv_up = (a >= 5)  # will take entries from a that are less than or equal to 5
print(fiv_up)   # bool array deducing condition of every a element
print(a[fiv_up])    # will print numerical value of elements true to condition
# using logical operators
b = a[(a > 2) & (a < 11)]       # a[ -- ] will provide numerical values
print(b)
fiv_up = (a > 5) | (a == 5)     # will give bool answers
print(fiv_up)
c = np.nonzero(a < 5)   # mark indexes that satify condition, for each tuple
print(c)

listOfCord = list(zip(c[0], c[1]))  # zip takes cartesian prod
for coord in listOfCord:
    print(coord)
print(a[c])
# command shows the case in which no element satisfies condition
void = np.nonzero(a == 42)
print(void)



