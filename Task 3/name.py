name = "ada lovelace"
print(name.title())  # function will print first alphabet as upper case
# change all characters to lowercase, uppercase respectively
print(name.upper())
print(name.lower())

first_n = "Mahrukh"
middle_n = "khan"
last_n = "niazi"
# concatenation
full_n = first_n + " " + middle_n + " " + last_n

print(full_n)
print("Hello ! " + full_n + "!")
print("Courses in my semester:\tComputer Networks\tTheory of Automata\tVisual Programming")

full_n.strip()  # deletes all whitespaces
print(full_n)

author = "Joseph Sugarman"
quote = "time's arrow neither stands still nor reverses. It merely marches forward. "
print(author + " once said " + quote)

name = "   Bojack\t  Horseman  "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
