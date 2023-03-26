# 10-8
filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    print("\nReading file: " + file)
    try:
        with open(file) as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("error 404")

# 10-9 modifying last excercise
for file in filenames:
    try:
        with open(file) as f:
            data = f.read()
    except FileNotFoundError:
        pass
    else:
        print("\nReading file: " + file)
        print(data)

# 10-10
def count_comm_words(filename, word):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)

filename = 'alice.txt'
count_comm_words(filename, 'the')