import pickle

student = {1: 'mark', 2: 'jhon', 3:'alex'}

# with open('student.pkl', 'wb')as pick:
#     pickle.dump(student, pick)
#

# unpickling

with open('student.pkl', 'rb')as pick:
    stdlist = pickle.load(pick)

print(stdlist)