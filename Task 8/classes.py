#  init function is your constructor that calls itself
# whenever object of that clss is made

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " has rolled over!")


# objects :  instance of a class
dogo = Dog('rocky', 5)
print("Dogos name is : " + dogo.name.title())
print("Its age is : " + str(dogo.age))

# attributes can be accessed by obj name + dot operator

# calling methods
dogo.roll_over()
dogo.sit()

dogy = Dog('jeremy', 16)
print("My friends dog name is : " + dogy.name.title())
print("She is " + str(dogy.age) + "years old")

