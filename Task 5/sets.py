# Learning aid for built-in functions website:
# https://www.programiz.com/python-programming/set#:~:text=Create%20a%20Set%20in%20Python,tuple%2C%20string%20etc.).
# operations sets aid in providing:-
# | for union.
# & for intersection.
# – for difference
# ^ for symmetric difference
# we can also use symbols and also use the python library

# Sets are data structures that,based on specific
# rules they define, provide certain cool operations.

# checking element existence in set has (0(1)) time complexity
# cannot create empty set with curly braces
# set constructor is used, they are collections hence iterable

toy1 = {'donkeykong', 'mario', 'luigi'}     # valid set creation
# multiple data type sets
mixed_set = {'hello', 78, -12.5, 'Clean shave'}
print(mixed_set)
toys = set(['barbie', 'dinosaur', 'buzz Lightyear', 'ken'])
print("These are my toys!")
for toy in toys:
    print(toy)

# formatted output
for t in toys:
    print('This is my toy: {}'.format(t))

# INTERSECTION & : prints elements present in both sets

a = set([2, 3, 4, 5])
b = set([2, 5, 6, 7])

print("set a : ", str(a))
print("set b : ", str(b))

result = a.intersection(b)
# result = b.instersection(a) will also work
# commutative nature
print(str(result), "Are present in both sets ( intersection )")

# UNION | : concatenation of sets , without iteration redundant elements

result = a.union(b)
# result = b.union(a) valid , commutative nature
print(str(result), "Are the elements in sets a , b ( union )")

# DIFFERENCE - : stores elements from set 1 that are not present in set 2
# not commutative

result = a.difference(b)
print(str(result), "Elements not in b ( difference )")

result = b.difference(a)
print(str(result), "Elements not in a ( difference )")

# SYMMETRIC DIFFERENCE ^
# we take comparison of same index elements to see if they are present in
# the same position as of other set
# definition : sets which contain the elements which are either in set A or in set B
# but not in both

result = a.symmetric_difference(b)
# result = b.symmetric_difference(a) will give same answer as commutative nature
print(str(result), "is symmmetric difference b/w set a b ( symmetric difference )")


# empty set
empty_s = set()
print(type(empty_s))

# duplicate items in set , unique nature
numb = set([2, 4, 5, 6, 6, 7, 8, 2, 1])
print("initial set: ", str(numb))
numb.add(89)
print("Updated set: ", str(numb))
numb.discard(6)
print("Updated set after discarding: ", str(numb))