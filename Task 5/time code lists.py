# checking time execution time for creating lists

import time

start = time.time()     # sets ticks
print("Initial time: ", start)
A = ['Cats', 'dogs', 'fish']
print("List A = [] execution time", time.time() - start, " seconds")
start2 = time.time()
A1 = list(['catu', 'dogu', 'fishy'])
print("List A = list() execution time", time.time() - start2, " seconds")

# local time :

locTime = time.asctime(time.localtime(time.time()))     # asc time formats from double
print(locTime)