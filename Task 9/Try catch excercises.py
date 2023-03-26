# 10-6
try:
    x = input("Give me 1 number: ")
    x = int(x)
    y = input("Give me 1 more number: ")
    y = int(y)
except ValueError:
    print("Sorry, I needed a number :(.")

else:
    add = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(add) + ".")

# 10-7

print("Enter 'q' at any time to quit.\n")
while True:
    try:
        x = input("\nGive 1 number: ")
        if x == 'q':
            break
        x = int(x)
        y = input("Give 1 more number: ")
        if y == 'q':
            break
        y = int(y)      # else explicit type cast into y variable
    except ValueError:
        print("Sorry, I wanted a number :(.")
    else:
        add = x + y
        print("The sum of " + str(x) + " and " + str(y) + " = " + str(add) + ".")
    