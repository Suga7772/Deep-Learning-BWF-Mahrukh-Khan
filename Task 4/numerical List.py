# 4-3
for num in range(1, 21):
    print(num)

# 4-5

mil = list(range(1, 1000001))
print(min(mil))
print(max(mil))
print(sum(mil))

# 4-6  odd numbers from 1-20

for value in range(1, 20, 2):
    print(value)
# 4-7

mul = list(range(3,31,3))
for number in mul:
    print(number)

# 4-8 Cubes
cube = []
for num in range(1, 11):
    c = num**3       #taking cube
    cube.append(c)   #ADD AT END

#show display cubes
for loop in cube:
    print(loop)

# 4-9 Cube comprehension
num = [n**3 for n in range(1,11)]
#display
for n in num:
    print(n)



