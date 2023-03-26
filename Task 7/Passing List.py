def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


user = ['bilal', 'vix', 'suga']
greet_users(user)


# examples

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# TRY IT YOURSELF

# 8-9 magicians woooo
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ['Ooga Booga', 'Madonna', 'Pennywise']
show_magicians(magicians)


# 8-10 great magicians!

def make_great(magicians):      # append the great at the end of each magic person name
    great_magicians = []  # EMPTY LIST
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['Ooga Booga', 'Madonna', 'Pennywise']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

# 8-11
# reusing functions from previous try it yourself excercises

def make_great1(magicians):
    great_magicians = []    # empty list
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    # Append the great magicians into the list
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

magicians1 = ['Ooga Booga', 'Madonna', 'Pennywise']
show_magicians(magicians1)
print("\nGreat magicians:")
great_magicians = make_great1(magicians1[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(magicians1)