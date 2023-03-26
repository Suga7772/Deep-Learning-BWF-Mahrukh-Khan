def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# This is an infinite loop
while True:
    print("\nPlease tell me your name:")
    print("Press 'q' any time to quit")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# TRY IT YOURSELF
# 8-6 city name

def city_country(city, country):
    return city + ", " + country


c1 = city_country('karachi', 'pakistan')
print(c1)
c2 = city_country('tokyo', 'japan')
print(c2)
c3 = city_country('mumbai', 'india')
print(c3)


# 8-7 album
def make_album(name, title):
    album = {'album-artist': name, 'album-title': title}
    return album


a = make_album('freddie', 'hotspace')
print(a)
b = make_album('shakira', 'dance the night away')


def make_album1(name, title, tracks=0):
    album = {'album-artist': name, 'album-name': title}
    if tracks:
        album['tracks'] = tracks
    return album


a1 = make_album1('shakespeare', 'mozart', 8)
print(a1)


# 8-8

def make_album(artist, title, tracks=0):
    album_dict = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

# out of functioin
# Let the user know how to quit.
print("Enter 'quit' at any time to stop the loop.")
while True:
    title = input("What album are you thinking of? ")
    if title == 'quit':
        break
    artist = input("Who's da singer? ")
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)

print("\nGoodbye")
