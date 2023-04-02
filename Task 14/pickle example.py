import pickle
car = ['bmw', 'mercedes', 'toyota', 'subaru']

# pickling
# make file to store byte streams or list
# wb = write binary
# with open('car.txt', 'wb')as file:
#     pickle.dump(car, file)
#   code above commented as we have done pickling

# unpickling
# rb = read binary
with open('car.txt', 'rb')as mypickle:
    mycar = pickle.load(mypickle)

print(mycar)


