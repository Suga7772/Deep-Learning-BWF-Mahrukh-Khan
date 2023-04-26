import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as kncls
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

digit = load_digits()
print(digit.target_names)
digit_data = pd.DataFrame(digit.data, digit.target)
print(digit_data.head())

print(digit_data.shape)   # the dimensions [row,column]
digit_data['target'] = digit.target    # creating a new column
print(digit_data.head())      # proof that new column is created
print(digit_data[digit_data.target == 1].head())
print(digit_data[digit_data.target == 2].head())

X1 = digit_data.drop(['target'], axis='columns')
Y1 = digit_data.target
x_train, x_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.2, random_state=1)
print(len(x_train))
print(len(x_test))

knn = kncls(n_neighbors=10) # arguement is the K value
knn.fit(x_train, y_train)
print("Test with k=10: ", knn.score(x_test, y_test))

y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)       # diagonals correct prediction, not on diagonal is wrong prediction
# sum of all values wil equate to sample data , here it is 30

print(classification_report(y_test, y_pred))

# TESTING WITH K = 5
knn = kncls(n_neighbors=5) # arguement is the K value
knn.fit(x_train, y_train)
print("Test with k=5: ", knn.score(x_test, y_test))

y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)       # diagonals correct prediction, not on diagonal is wrong prediction
# sum of all values wil equate to sample data , here it is 30

print(classification_report(y_test, y_pred))

