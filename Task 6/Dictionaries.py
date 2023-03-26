# dictionaries help model real world objects in a more realistic manner
# collection of key value pairs , each key connects with a value
# dynamic , can manipulate at any given time
alien_0 = { 'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# bang bang alien
print("You shot the "+ str(alien_0['color'] + " alien!\nYou got " + str(alien_0['points']) + " points!"))

print(alien_0)
# add new key pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modifying key values in dictionary

print("The color of alien is: " + str(alien_0['color']))
alien_0['color'] = 'yellow'
print("The updated color of alien is: " + str(alien_0['color']))

# overriding key values of alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position of alien: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_inc = 1
elif alien_0['speed'] == 'medium':
    x_inc = 2
else:
    x_inc = 3

print("New alien position : " + str(alien_0['x_position'] + x_inc))

# update existing key values
alien_0['speed'] = 'fast'

# deleting key value
alien_0 = { 'color ': 'green', 'points': 5}
print(alien_0)
del alien_0['points']       # permanent deletion
print(alien_0)

fav_lang = {'jen': 'c++', 'bilal': 'ruby', 'suga': 'python', 'saim': 'c#'}

print("suga's favourite language is : " + str(fav_lang['suga'].title()))
print("Bilal's favourite language is : " + str(fav_lang['bilal'].upper()))

# TRY IT YOURSELF

# 6-1
person = {'first_name': 'muhammad', 'last_name': 'mirza', 'age': 22, 'city': 'Rawalpindi'}
print("First name : " + person['first_name'].title() + "\nLast name: " + person['last_name'].title() + "\nAge: " + str(person['age']) + "\nCity: " + person['city'])

# 6-2
Fav_number = {'bilal': 55, 'mirza': 7, 'mahrukh': 9, 'saim': 17, 'zoya': 3}
print("Bilal's favourite number is " + str(Fav_number['bilal']))
print("Mirza's favourite number is " + str(Fav_number['mirza']))
print("Mahrukh's favourite number is " + str(Fav_number['mahrukh']))
print("Saim's favourite number is " + str(Fav_number['saim']))
print("Zoya's favourite number is " + str(Fav_number['zoya']))


# 6-3 Glossary
glossary = {'set': 'collection of non iterable elements', 'input()': 'takes user input from terminal of any data type',
         'if': 'condition checking , initial block',
         'elif': 'else if block , for calculating if the "if" clause is false',
         'for': 'loop iterator that iterates each element of a set, collection'}

print("Set : \n" + glossary['set'] + "\ninput() : \n" + glossary['input()']
      + "\nif : \n" + glossary['if'] + '\nelif : \n' + glossary['elif'] +
      "\nfor : \n" + glossary['for'])


