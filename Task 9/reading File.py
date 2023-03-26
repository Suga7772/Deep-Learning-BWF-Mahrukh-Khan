with open('pi_digits.txt') as file_obj:
    contents = file_obj.read()
    print(contents)
    print(contents.rstrip())    # removes white spaces

# file paths
# with open('text_file\filename.txt') as file_obj
# ^^ someitmes we need to have a directory structure to
# navigate the file

# windows its \
# linux, IOS its / for directing subdirectories

filen = 'pi_digits.txt'

with open(filen) as file_obj:
    for line in file_obj:
        print(line.strip())

# making list of lines
with open(filen) as file_obj2:
    lines = file_obj2.readlines()
for line in lines:
    print(line.rstrip())


# working with file contents
filename = 'pi_digits.txt'
with open(filename) as file_obj1:
    lines = file_obj1.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

