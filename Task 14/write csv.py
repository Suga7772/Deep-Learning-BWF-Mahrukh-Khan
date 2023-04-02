import csv

with open('examples/ex1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["a", "b", "c", "d", "message"]

    writer.writerow(field)
    writer.writerow([1, 2, 3, 4, "hello"])
    writer.writerow([5, 6, 7, 8, "world"])
    writer.writerow([9, 10, 11, 12, "foo"])

# file without header
with open('examples/ex2.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow([1, 2, 3, 4, "hello"])
    writer.writerow([5, 6, 7, 8, "world"])
    writer.writerow([9, 10, 11, 12, "foo"])

# heirarchial index
with open('examples/csv_mindex.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["key1", "key2", "value1", "value2"]

    writer.writerow(field)
    writer.writerow(['one', 'a', 1, 2])
    writer.writerow(['one', 'b', 3, 4])
    writer.writerow(['one', 'c', 5, 6])
    writer.writerow(['one', 'd', 7, 8])
    writer.writerow(['two', 'a', 9, 10])
    writer.writerow(['two', 'b', 11, 12])
    writer.writerow(['two', 'c', 13, 14])
    writer.writerow(['two', 'd', 15, 16])

with open('examples/ex4.csv', 'w', newline='') as file:
    # hey
    writer = csv.writer(file)
    field = ["a", "b", "c", "d", "message"]
    # just wanted to make things difficult for you
    # who reads csv files with computers anyway?
    writer.writerow(field)
    writer.writerow([1, 2, 3, 4, "hello"])
    writer.writerow([5, 6, 7, 8, "world"])
    writer.writerow([9, 10, 11, 12, "foo"])


with open('examples/ex5.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["something", "a", "b", "c", "d", "message"]

    writer.writerow(field)
    writer.writerow(["one", 1, 2, 3, 4, ])
    writer.writerow(["two", 5, 6,None,8, "world"])
    writer.writerow(["three", 9, 10, 11, 12, "foo"])