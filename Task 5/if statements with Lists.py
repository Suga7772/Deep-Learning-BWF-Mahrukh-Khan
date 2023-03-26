toppings = ['mushrooms', 'jalapeno', 'olives', 'pineapple']

for topping in toppings:
    if topping == 'jalapeno':
        print("Ah we are out of this toppping")
    else:
        print("Adding "+topping+" in pijja")

print("finished Ballerinas Pizza")

# checking empty lists
top = []
if top:
    print("Adding " + top + " in pijja")
else:
    print("You want no toppings?")

# working with Multiple Lists
available_toppings = ['shrimps', 'oysters', 'pineapple', 'olives', 'szechuan peppercorn']
req_topping = ['mushrooms', 'olives', 'pineapple', 'fries']

for top in req_topping:
    if top in available_toppings:
        print("Adding " + top + " in Ballerinas Pizza")
    else:
        print("Sorry vix didnt stock up the " + top + " toppings")

print("Finished making pizza")


# TRY IT YOURSELF
# 5-8
username = ['bilal', 'suga', 'vix', 'admin', 'tunechi']

for user in username:
    if user == 'admin':
        print("HIIII ADMIN SIR ")
    else:
        print("Nice to have you back, " + user)

# 5-9
# checking if username list is not empty
if username:
    print("Got alotta users here")
else:       # denotes empty list
    print("We need users!!")

username.clear()        # emptied the string
if username:
    print("Got alotta users here")
else:  # denotes empty list
    print("We need users!!")


# 5-10
current_users = ['bilal', 'suga', 'vix', 'admin', 'tunechi', 'Jhon']
new_users = ['amjad', 'umi', 'vix', 'BILAL', 'cody', 'jhon']
# case insensitive logic
for new in new_users:
    if new in current_users:
        print("User name " + new + " unavailable")
    elif new.upper() in current_users:
        print("User name " + new + " unavailable")
    elif new.lower() in current_users:
        print("User name " + new + " unavailable")
    elif new.title() in current_users:
        print("User name " + new + " unavailable")
    else:
        print("user name "+ new +" is available")

# 5-11 Ordinal numbers

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in num:
    if n == 1:
        print(str(n) + "st")
    elif n == 2:
        print(str(n) + "nd")
    elif n == 3:
        print(str(n) + "rd")
    else:
        print(str(n) + "th")

# 5-12 dunzo
# 5-13
# I want to make condition based approach to morning routine
# in lieu with the time you wake up , if you wake up at the ideal
# time i.e 1 hour before work , you can work out , shower eat breakfast
# before going to work. If time of waking up is 30 minutes before work
# then shower and breakfast is feasible, and in the often cases of 15 mins
# till work time you can only eat breakfast (as breakfast in my eyes is prioritised
# the most in this case. And unfortunately if you wake up 5 minutes before work time
# you have to RUNNNN!!!
