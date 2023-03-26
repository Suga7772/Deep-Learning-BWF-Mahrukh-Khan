class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('lamborghini', 'b4', 2020)
print(my_new_car.get_descriptive_name())


# TRY IT YOURSSL
# 9-4 number served , uising resteraunt class as prior
class Restauranto():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = self.name + " has amazing " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        msg = self.name + " is open!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restauranto('flamboyant Mercury', 'baba Ganoush')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 420
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(127)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(619)
print("Number served: " + str(restaurant.number_served))
