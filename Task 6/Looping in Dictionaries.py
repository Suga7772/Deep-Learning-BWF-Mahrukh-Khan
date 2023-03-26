
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# if looping instance, the pairs are not in the set order displayed, it's not an issue as the python
# interpreter only connects the pairs with each other and not the exact location in a sequence
# key is the attribute, value is the right of the pair
for key, value in user.items():
    print("\nKey : " + key)
    print("Value : " + value)

fav_lang = {'jen': 'c++', 'bilal': 'ruby', 'suga': 'python', 'saim': 'c#'}

for name, lang in fav_lang.items():
    print(name + " Fav lang is : " + lang)

# items function helps take both key and value
# keys function only allows value to be fetched in a dictionary

for lang in fav_lang.keys():
    print(lang.title())

# for lang in fav_lang: will have the same effect as above for loop

if 'Erin' not in fav_lang.keys():
    print("Take the poll Erin!")

if 'Erin' not in fav_lang:
    print("Take the poll Erin!")

# ordered looping

for name in sorted(fav_lang.keys()):
    print(name + ",Thank you for being my friend")

# accessing only values (right side) in a dictionary
for name in fav_lang.values():
    print(name)

# we can use set to remove any redundancy

fav_lang = {'jen': 'python', 'bilal': 'ruby', 'suga': 'python', 'saim': 'c#'}
print("Following values have been mentioned: \n")
for lang in set(fav_lang.values()):
    print(lang)

# TRY IT YOURSELF
# 6-4
glossary = {'set': 'collection of non iterable elements', 'input()': 'takes user input from terminal of any data type',
         'if': 'condition checking , initial block',
         'elif': 'else if block , for calculating if the "if" clause is false',
         'for': 'loop iterator that iterates each element of a set, collection'}

for key, value in glossary.items():
    print(key + " : " + value + "\n")

glossary = {'set': 'collection of non iterable elements', 'input()': 'takes user input from terminal of any data type',
         'if': 'condition checking , initial block',
         'elif': 'else if block , for calculating if the "if" clause is false',
         'for': 'loop iterator that iterates each element of a set, collection',
            '==': 'conditional equality checker from both values that are on either side',
            'print()': 'output command , will print everything encapsulated insaide circle brackets in form of a string',
            'list': 'mutable data structure', 'not in ': 'condition checker, similar to != operation',
            'split()': 'seperates data of a string from empty spaces '}

for key, value in glossary.items():
    print(key + " : " + value + "\n")

# 6-5
major_river = {'nile': 'egypt', 'indus': 'south-Asia', 'sutlej': 'pakistan'}

for riv, place in major_river.items():
    print(riv + " flows in " + place)

# printing rivers only
for key in major_river:
    print(key)

# printing places only
for val in major_river.values():
    print(val)

# 6-6

fav_lang = {'jen': 'c++',
            'bilal': 'ruby',
            'suga': 'python',
            'saim': 'c#'}

fav_lang_Poll = ['amjad', 'bobby', 'carrie', 'saim', 'alex', 'bilal']
for name in fav_lang_Poll:
    if name in fav_lang.keys():
        print("hey " + name + " thanks for taking the poll")
    else:
        print(" You should take the poll, " + name + " ! ")
