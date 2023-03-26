# enumerate built-in function
# https://blog.hubspot.com/website/python-enumerate#:~:text=The%20enumerate%20function%20in%20Python,the%20collection%20easier%20to%20access.
# converts a tuple (collection) into an enumerate object
# each element in a tuple will be rewarded an index

fruits = ('cherry', 'durian', 'avocado')
emojis = (':/', ';)', ':*', ':D', ':(', ':O')

enu = enumerate(fruits)
enu1 = enumerate(emojis)

print(list(enu))
print(list(enu1))
print(enumerate(fruits, 2))  # shows memory location of it

snekTuple = ("conda", "python", "snekie")
for run in enumerate(snekTuple):
    print(run)
