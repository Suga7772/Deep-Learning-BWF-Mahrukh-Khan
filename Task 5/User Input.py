# how to take values , or data to store eventually in a variable/tuplee/list
import math

# input ( everything ecapsulated inside here is the )
#single inputs
# by default, input or any variable is considered a string
# string input
username = input("Enter your name , you beauty: ")
# integer input
num = int(input("Enter your age: "))
# float input
radius = float(input("Enter radius of circle: "))
print("Hi " + username + " your " + str(num) + " years young")
print("Area of circle: ", str(math.pi * (radius**radius)))
print("Name is : ", type(username))
print("age is : ", type(num))
print("radius is: ", type(radius))

# taking multiple inputs

x, y = input("Enter two values: ").split()        # enter one number , press space as to input second number
print("First num: ", x)
print("Second num: ", y)

# taking n number of inputs
# uses listand split to seperate with spaces

#string
fruit = list(input("Enter fruits ! ").split())
print("Fruits: ", fruit)

# integer , takes map function for explicit typecast
marks = list(map(int, input("Enter your course marks: ").split()))
print("Marks: ", str(marks))