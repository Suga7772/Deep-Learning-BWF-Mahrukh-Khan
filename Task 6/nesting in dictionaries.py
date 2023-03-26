alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points':  '7'}
alien_2 = {'color': 'pink', 'points': '18'}

# adding all dictionaries in a list
aliens = [alien_0, alien_1, alien_2]
# displaying the list
for alien in aliens:
    print(alien)

aliens  =[]
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '6'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("....")

print("Total number of aliens created: " + str(len(aliens)))

aliens = []
# maketh 30 green aliens
for alien_number in range(0,30):
    new_a = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_a)
# modifying the first 3 dictionaries
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'fast'

for alien in aliens[0:5]:
    print(alien)
print("....")


# looping through list

pizza = {'crust': 'thin', 'toppings': ['olives', 'jalapeno']}

# order summary
print("Order up! a " + pizza['crust'] + " crust with toppings : ")
for top in pizza['toppings']:
    print("\t" + top)

fav_lang = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, lang in fav_lang.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in lang:
        print("\t" + language.title())

# dictionary in a dictionary

users = {
    'ainstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
       }

for username, user_info in users.items():
    print("User : " + username)
    name = user_info['first'] + " " + user_info['last']
    loc = user_info['location']
    print("\tFull name : " + name.title())
    print("\tLocation: " + loc.title())

