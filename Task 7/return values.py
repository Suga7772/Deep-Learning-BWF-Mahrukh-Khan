def get_Full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_Full_name('Freddie', 'Mercury')
print(musician)


# optional arguments

def get_optionFull_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


artist = get_optionFull_name('Jamie', 'lee', 'Anderson')
print(artist)


# let us make middle names default
def get_optionFull_name(first_name, last_name, middle_name=" "):
    # if we have non default middle name
    if middle_name:
        f = first_name + ' ' + middle_name + ' ' + last_name
    else:
        f = first_name + ' ' + last_name
    return f.title()


singer = get_optionFull_name('ellie', 'goulding')
print(singer)
singer = get_optionFull_name('zoya', 'fajar', 'khan')
print(singer)


# returning dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person.title()


artist = build_person('jimi', 'hendrix')
print(artist)
