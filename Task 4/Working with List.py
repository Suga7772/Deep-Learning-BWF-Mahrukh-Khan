# 4-10 Slices
places = ["Birmingham", "Greece", "Italy", "Brazil", "Hokkaido"]
print(places[0:4])
print(places[2])
print(places[2:])

# 4-11 my pizza , your pizza
fav_pizzas = ['neopolitan', 'italian', 'thin-crust']
friend_pizzas = fav_pizzas[:]

fav_pizzas.append("Deep Dish")
friend_pizzas.append('Tikka')

print("My favorite pizzas are:")
for pijja in fav_pizzas:
    print(pijja)

print("\nMy friens favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12 More loops
food = [ [1, 2, 3, 4, 5], ["Brocolli", "Avocado", "Turnip","Zuccinni","Tomato"]]

for i in range(len(food)):
    for j in range(len(food[i])):
        print(food[i][j], end='\n')
    print()