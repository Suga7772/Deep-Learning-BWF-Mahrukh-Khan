file = 'learning_python.txt'
print("Reading in the entire file:")
with open(file) as f:
    data = f.read()
print(data)

print("\nLoop lines:")
with open(file) as f:
    for line in f:
        print(line.rstrip())

print("\nStoring the lines in a list:")
with open(file) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())    # showcasing the lines we have written in a string

print("\n\n\n")
# 10-2
with open(file) as f:
    line1 = f.readlines()

for line in line1:
    # remove newline,replace Python with C character.
    line = line.rstrip()
    print(line.replace('Python', 'C'))  # case sensitive