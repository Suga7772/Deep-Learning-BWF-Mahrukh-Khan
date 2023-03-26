import json

with open('favorite_number.json') as f:
    number = json.load(f)

print("your favorite number is: " + str(number) + ".")