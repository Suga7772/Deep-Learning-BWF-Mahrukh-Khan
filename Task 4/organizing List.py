# Mahrukh khan 19th March 2023
# TRY IT YOURSELF

visit = ['Austrailia', 'Japan', 'Brazil', 'France', 'Alabama']
print(visit)

print("Temporary sort : ")
print(sorted(visit))

print("List in original order : ")
print(visit)

print("\nTemporary reserve sort : ")
print(sorted(visit,reverse=True))
print("List in original order : ")
print(visit)

visit.reverse()
print("\nOrder changed : ")
print(visit)
visit.reverse()
print("Order back to original: ")
print(visit)

visit.sort()
print("\nSorted in alphabetical order: ")
print(visit)

visit.sort(reverse=True)
print("\nSorted in reverse alphabetical order: ")
print(visit)

guest_list = ['rakeen', 'freddie', 'ballerina', 'Madonna', 'Hitler']
print("im inviting " + str(len(guest_list)) + " guests for dinner")
