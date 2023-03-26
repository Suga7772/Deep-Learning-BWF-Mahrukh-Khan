# 9-8

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
        self.privileges = Privileges()  # initialise empty set of privileges


# seperate class privilegge
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_priv(self):
        print("\nPrivileges:")
        if self.privileges:
            for p in self.privileges:
                print(p)
        else:
            print("user got no privileges.")


# suga is obj of admin class
suga = Admin('suga', 'works', 'S_works', 'SugaisBomb@example.com', 'antonito')
suga.describe_user()
# making privileges
suga_privileges = ['can delete users', 'permission to suspend accounts', 'changing password']

suga.privileges.privileges = suga_privileges
suga.privileges.show_priv()

# 9-9
class Car():

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        lname = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return lname.title()

class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("car got a " + str(self.battery_size) + "kWh battery.")

    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185

        print("car can run " + str(range)+" miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("battery already upgraded.")


class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("CREATE ELECTRIC CAR TO TRY AGAIN:")
elec = ElectricCar('fuzzy', 'model A', 2022)
elec.battery.describe_battery()

print("\nCHECK AFTER UPGRADING BATTERY:")
elec.battery.upgrade_battery()
elec.battery.describe_battery()

print("\nUPGRADING BATTERY 2ND TIME.")
elec.battery.upgrade_battery()
elec.battery.describe_battery()