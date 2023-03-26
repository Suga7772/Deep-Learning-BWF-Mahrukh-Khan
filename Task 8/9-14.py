from random import randint

class Die():
    def __init__(self, sides=6):     #default sides 6
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)   # range defined in parentheses 1 to sides



# 6-side die,results of 10 rolls.

die6 = Die()

res = []        #empty list to store the values in
for roll_num in range(10):
    res1 = die6.roll_die()
    res.append(res1)
print("10 rolls result of 6 side die:\n")
print(res)

# 10-sided die,results of 10 rolls.
die10 = Die(sides=10)

res = []
for roll_num in range(10):
    res1 = die10.roll_die()
    res.append(res1)
print("10 rolls result of a 10-sided die:\n")
print(res)

# 20-sided die,results of 10 rolls.

die20 = Die(sides=20)
res = []
for roll_num in range(10):
    res1 = die20.roll_die()
    res.append(res1)
print("\n10 rolls result of a 20-sided die:")
print(res)


# 9-15 Python module of the week explored yay
