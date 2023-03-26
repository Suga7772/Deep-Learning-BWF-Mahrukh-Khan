# we would get error in print(5/0) statementso we need try catch block
# to handle such exceptions

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# division practice
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# handling file not found exception
filename = 'alice_in_wonderland.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry your file " + filename + " does not exist"
    print(msg)


# working with multiple files
def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'sidhartha.txt', 'prog Poll.txt', 'pi_digits.txt']
count_words(filenames)

