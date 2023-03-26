name = input("What is your pretty name? ")
filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name + "\n")

# 10-4
print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + "\n")
        print("Hi " + name + ", you've been added to the guest book.")


# 10-5 programming poll
file = 'prog Poll.txt'

print("Enter 'q' when you are finished.")
while True:
    reason = input("\nWhy do you like programming ")
    if reason == 'q':
        break
    else:
        with open(file, 'a') as f:
            f.write(reason + "\n")
        print("Added to the poll")
