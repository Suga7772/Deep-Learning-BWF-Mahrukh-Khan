# TRY IT YOURSELF
# 9-1
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + " has sizzling " + self.cuisine_type + "."
        print(msg)

    def open_restaurant(self):
        msg = self.name + "IS SERVING OPEN RN"
        print("\n" + msg)


restaurant = Restaurant('killer combo', 'cheese burger')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2

Marios = Restaurant("Super Marios", 'Italian pizza')
Marios.describe_restaurant()

Thai_leg = Restaurant('Thai Fusion', 'Egg fried rice')
Thai_leg.describe_restaurant()

Gordon_Ramsay = Restaurant('Hells Kitchen', 'Beef Wellington')
Gordon_Ramsay.describe_restaurant()

# 9-3 users - make user profile in class
class User():
    def __init__(self, fname, lname, uname, email, location):
       # user initialisation
        self.first_name = fname.title()
        self.last_name = lname.title()
        self.username = uname
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
       print("\nOhayo Guzaimas, " + self.username + "!")

Suga = User('Suga', 'Works', 'e_matthes', 'S_Ugar@example.com', 'karachi')
Suga.describe_user()
Suga.greet_user()

Ballerina = User('ballerina', 'williams', 'Ball4Lyfe', 'Balerina702@example.com', 'toronto')
Ballerina.describe_user()
Ballerina.greet_user()