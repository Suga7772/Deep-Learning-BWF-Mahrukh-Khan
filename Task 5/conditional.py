# if and further conditions

careers = ['gymnast', 'dancer', 'scientist', 'cool guy', 'artist']

for career in careers:
    if career == 'dancer':
        print(career.upper())
    else:
        print(career.title())

# equality checking
# can be computed by ==
# assignment is done by =
# case-sensitive
# can temporarily change case of element for conditional checking without alternating whole element


# inequality
topping = 'mushrooms'
if topping != 'anchovies':
    print('Hold the anchovies!')

# numerical
ans = 77
if ans != 420:
    print("thats not the best number, Go again")

if ans > 420:
    print(ans, " > 420")
if ans < 420:
    print(ans, ' < 420')

# multiple condition checking , binary

a1 = 20
a2 = 23
if a1 >= 18 and a2 <= 23:
    print("haha binary conditionals and")

if a1 >= 18 or a2 <= 43:
    print("haha binary conditionals or")

# checking value in a list

if 'gymnast' in careers:
    print("We have a suga in the house!")
if 'driver' in careers:
    print("got a driver in the house!")

# checking non values in list

if 'driver' not in careers:
    print("nice, driver not in careers")

if 'artist' not in careers:
    print('nice artist, your not a viable career')

# boolean expressions
# can be either true or false
# keeps track of certain conditions

stop = True
# following loop will run till 10
for i in range(30):
    if stop:
        print(i)
    if i == 10:
        stop = False

# TRY IT YOURSELF
# 5-1

cat = 'chino'
print('is cat Tabby? maybe true')
print(cat == 'Tabby')       # false
print('is cat Bilal? maybe yes')
print(cat == 'Bilal')       # i wish ;-;
print('is cat Simon? maybe False')
print(cat == 'Simon')   # false
print('is cat Simba? maybe not')
print(cat == 'Simba')       # false
print('is cat Chino? maybe false')
print(cat.title() == 'Chino')       # true since we temporarily changed cat element to match
print('is cat chino? maybe true')
print(cat == 'chino')       # true
print('is cat Cappucino? maybe not')
print(cat == 'Cappucino')   # false
print('is cat CHINO? maybe YES')
print(cat.upper() == 'CHINO')   # true
print('is cat Cody? maybe True')
print(cat == 'Cody')       # false
print('is cat chino? maybe YES')
print(cat == 'chino')       # true

# 5-2

