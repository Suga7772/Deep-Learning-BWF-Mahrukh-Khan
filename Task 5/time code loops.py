# figuring out the exact time loops can counter in timing
import time

start = time.time()     # sets ticks
print(start)
count = 0

# for loop
for i in range(45):
    print("Hi this is my", i, "'th time asking you for a food date!")
print("For loop time: ", time.time() - start, " seconds")

# while loop
start2 = time.time()        # start ticks for assessing while loop
while count < 45:
    print("Hi this is my", count, "'th time asking you for a food date!")
    count += 1
print("For loop time: ", time.time() - start2, " seconds")
