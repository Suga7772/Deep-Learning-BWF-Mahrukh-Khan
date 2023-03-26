# 9-6 ice cream stand
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open!"
        print(msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='bbq'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nfollowing flavors are available:")
        for flavor in self.flavors:
            print(flavor.title())


i1 = IceCreamStand('Hunky dory')
i1.flavors = ['shamrock', 'irish pebbles', 'sour cherry']
i1.describe_restaurant()
i1.show_flavors()

# 9-7 Admin worky

class User():

    # constructor calls , initiliases all functionis with respective parameters
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("Location: " + self.location)

    def greet_user(self):
        print("\nWelcome " + self.username + "<3")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# inheritance child is admin , user is daddy
class Admin(User):

    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges -")
        for privilege in self.privileges:
            print(privilege)


suga = Admin('suga', 'works', 'S_works', 'SugaisBomb@example.com', 'antonito')
suga.describe_user()
suga.privileges = [  'can delete users', 'permission to suspend accounts', 'changing password',]
suga.show_privileges()