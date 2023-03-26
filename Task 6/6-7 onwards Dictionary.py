# TRY IT YOURSELF
# 6-7 People

person1 = {'first': 'mahrukh',
           'last': 'khan',
           'age': '20',
           'city': 'Rawalpindi'}
person2 = {'first': 'Aaron',
           'last': 'Sanchez',
           'age': '25',
           'city': 'Ali cante'}
person3 = {'first': 'Pedro',
           'last': 'Sanchez',
           'age': '23',
           'city': 'Portugal'}

people = [person1, person2, person3]

for pp in people:
    print(pp)

# 6-8 Pets

chino = {
    'kind': 'cat',
    'breed': 'tabby',
    'color': 'orange',
    'owner': 'mahrukh'
}
rocky = {
    'kind': 'dog',
    'breed': 'bullterrier',
    'color': 'white',
    'owner': 'saim'
}
Yuki = {
    'kind': 'cat',
    'breed': 'persian',
    'color': 'white',
    'owner': 'murtaza'
}
Skyler = {
    'kind': 'cat',
    'breed': 'siamese',
    'color': 'black',
    'owner': 'mirza'
}

pets = [chino, rocky, Yuki, Skyler]
for pet in pets:
    print(pet)

# 6-9
favorite_places = {'freddie': 'japan',
                   'zoya': 'tokyo',
                   'jennifer': 'osaka'}
print("\n")
for name, place in favorite_places.items():
    print(place + " is " + name + "'s favorite place")

# 6-10
favorite_number = {
    'jennifer': [9, 12],
    'marco': [12, 54],
    'julio': [3, 15],
    'tunechi': [90, 7]
}

print("Favourite numbers: ")

for name, num in favorite_number.items():
    print(name + "'s favourite numbers are : ")
    for n in num:
        print(n)

# 6-11
cities = {
    'oklahoma': {
        'country': 'america',
        'population': '12 million',
        'fact': 'has the most cotton production'
    },
    'karachi': {
        'country': 'Pakistan',
        'population': '20 million',
        'fact': "City of lights"
    },
    'ottawa': {
        'country': 'canada',
        'population': '8 million',
        'fact': 'hershey central',
    },
}

for city, key in cities.items():
    print("\n\n" + city.title() + " Information : \n")
    print("Country: " + key['country'])
    print("Population: " + key['population'])
    print("Fact: " + key['fact'])

# 6-12 extensions

# dictionary in a dictionary example redoing it to make it better

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
    'Jbaldwin': {
        'first': 'Joe',
        'last': 'Baldwin',
        'location': 'New York',
    },
    'Fmercury': {
        'first': 'Freddie',
        'last': 'Mercury',
        'location': 'Zanzibar',
    },
       }

for username, user_info in users.items():
    print("User : " + username)
    name = user_info['first'] + " " + user_info['last']
    loc = user_info['location']
    print("\tName : " + name.title())
    print("\tLocation: " + loc.title())
