# functions are designed to do one specific job within their block of code

def greet():
    # display welcome message
    print("Welcome!")


def greet1(user):
    # display welcome message
    print("Welcome!" + user)


greet1('amjad')
greet()


# 8-1
def display_message():
    print("I am learning fuinctions in python right now from this crash course book!")


display_message()


# 8-2

def favourite_book(name):
    print("My favourite book is " + name)


favourite_book(' mockingbird')


# passing arguements

def describe_pet(animal_type ,pet_name):
    print("\nMy animal is " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('cat', 'chino')

# multiple function calls
describe_pet('wolf', 'jacob')


# keyword arguments
describe_pet(animal_type='hamster', pet_name='vix')
# default values
def describe_pet(pet_name, animal_type='dog'):
    print("\nMy animal is " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='wonka')      # no issue as default dog in function arguements will beb invoked
