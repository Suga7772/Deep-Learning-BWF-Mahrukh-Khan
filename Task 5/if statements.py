# only goes in depth with if statements

age = 19
if age >= 18:
    # will run all script within if indent block ( spaced forward )
    print("Have you voted yet you", age, "year old?")
    print("did you register yet?")

# if else
# two blocks only evaluted, one after false condition of the first one
age = 17
if age >= 18:
    # will run all script within if indent block ( spaced forward )
    print("Have you voted yet you", age, "year old?")
    print("did you register yet?")
else:
    print("Go play outside kid")
    print("do vote whenever you turn 18 kiddo")

# if-elif-else chain
# when we need to evaluate more then two possible situations

# amusement park example
age = 12
if age < 4:
    print("4 year old , your admission is $0")
elif age < 18:
    print("hey teen, you gotta cough up $10 admission fees")
else:
    print("Admission cost for adults like YOU is 15 dolla")

# multiple elif blocks , yowza alotta possibilities to check

age = 40
if age < 10:
    price = 5
elif age < 20:
    price = 12
elif age < 30:
    price = 16
else:
    price = 20

print("Admission cost is " + str(price)+ " dollars")

# in some cases the else block is not mandatory as long as an elif
# block can satisfy specific / general else cases conditionals
# else is a catch call statement
# in if-elif block , rest blocks would end if our 'if' passes true

