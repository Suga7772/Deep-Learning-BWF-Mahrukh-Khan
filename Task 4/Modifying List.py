rides = ['civic', 'scooter', 'rickshaw', 'van']
print(rides)

# modify existing element
rides[3] = 'supra'
print(rides)

# append elements to list
rides.append('lamborghini')
print(rides)

# insert , will shift the existing elements to the right
rides.insert(0, 'bus')
print(rides)

# removing elements
del rides[0]
print(rides)

# can also delete last entry using pop
rides.pop()
print(rides)

# if we assign index then can pop exact element
popped = rides.pop(2)
print("The vehicle that i am gonna ride rn is " + popped )

# TRY IT YOURSELF

guest_list = ['rakeen', 'freddie', 'ballerina']
print("\nINVITATION FOR DINNER PARTY")
print("Hi " + guest_list[0] + " Your invited for dinner!")
print("Hi " + guest_list[1] + " Your invited for dinner!")
print("Hi " + guest_list[2] + " Your invited for dinner!")

print("\nIm sorry to notify that " + guest_list[0] + " cannot make it so i have invited another person!")
guest_list[0] = 'Hitler'

print("\nINVITATION FOR DINNER PARTY")
print("Hi " + guest_list[0] + " Your invited for dinner!")
print("Hi " + guest_list[1] + " Your invited for dinner!")
print("Hi " + guest_list[2] + " Your invited for dinner!")


print("\nYAYY I HAVE FOUND BIGGER TABLE")
guest_list.insert(0, 'Madonna')
guest_list.insert(2, 'Bilal')
guest_list.append('Micheal')

print("INVITATION FOR DINNER PARTY")
print("Hi " + guest_list[0] + " Your invited for dinner!")
print("Hi " + guest_list[1] + " Your invited for dinner!")
print("Hi " + guest_list[2] + " Your invited for dinner!")
print("Hi " + guest_list[3] + " Your invited for dinner!")
print("Hi " + guest_list[4] + " Your invited for dinner!")
print("Hi " + guest_list[5] + " Your invited for dinner!")

print("\nDang ! now my table has shrunk! sorry guests")
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

print("\nHi " + guest_list[0] + " Your still invited for dinner!")
print("Hi " + guest_list[1] + " Your still invited for dinner!")

del guest_list[0]
del guest_list[0]

print(guest_list)   # empty string
