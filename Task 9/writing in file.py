filen = 'programming.txt'

with open(filen, 'w') as file_object:       # w is permission to write
    file_object.write("I love programming.\n")
    file_object.write("My favourite language is Python\n")
    file_object.write("Game development is my hobby\n")
    file_object.write("I love being a vixen\n")

# appending in file

with open(filen, 'a') as file_object:       # will not override previous data in file
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")