def make_pizza(*toppings):
    print("Making pizza with the following toppings: ")
    for top in toppings:
        print(top)


make_pizza('dill pickles')
make_pizza('mushrooms', 'green peppers', 'olives')


# two arguments with one being arbituary value
def make_pizza(size, *toppings):
    print("\nMakin " + str(size) + " inch pizza with the following toppings:")
    for top in toppings:
        print(top)


make_pizza(20, 'pepperoni')
make_pizza(8, 'olives', 'dill pickles', 'parmeasan')


# dictionary based
def build_profile(first, last, **user_info):
    profile = {}  # empty dictionary
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


# TRY IT YOURSELF

# 8-12 Sammich
def make_sandwich(*items):
    print("\nLets make em sammiches:")
    for item in items:
        print(" We will add" + item + " to da sandwich.")


make_sandwich('fajita', 'gouda', 'cabbage', 'dill pickle')
make_sandwich('hunter beef', 'peaches', 'siracha')  # spoicy
make_sandwich('Peanut satay', 'grape jello')


# 8-13
def build_profile(first, last, **user_info):
    profile = {}  # empty dictionary
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Mahrukh', 'Khan', location='Rawalpindi', field='computer science',
                             hobbies='Swimming dancing')
print(user_profile)


# 8-14
def make_car(manufacturer, model, **options):
    car_dict = {'make': manufacturer.title(), 'model': model.title()}
    for option, value in options.items():
        car_dict[option] = value
    return car_dict


vroomVroom = make_car('subaru', 'convertible', color='yellow', eletric=True)
print(vroomVroom)
kar = make_car('Civic', 'hatch back', year=2001, color='silver',
               windows='bulletproof and tinted')
print(kar)
