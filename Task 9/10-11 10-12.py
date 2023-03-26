# 10-11 ,favourite number remembering

import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("We will keep that in mind")

# 10-12 doing previous task but together in same program
import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Enter your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("I'll keep that in mind")
else:
    print("your favorite number is " + str(number) + ".")