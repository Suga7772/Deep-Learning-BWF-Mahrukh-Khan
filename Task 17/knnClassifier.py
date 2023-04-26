# resources : https://youtu.be/CQveSaMyEwM
# don't use  knn on big datasets, supervised learning model , figure out most nearby datapoint
# and figure out the maximum number
import pandas as pa
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as kncls
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

neigh = kncls(n_neighbors=3)    # k=3
neigh.fit(X, y)

print(neigh.predict([[1.1]]))
print(neigh.predict_proba([[0.9]]))

iris = load_iris()
# features: sepal, petals
print(iris.feature_names)
print(iris.target_names)
data = pd.DataFrame(iris.data, columns=iris.feature_names)
print(data.head())

print(data.shape)   # the dimensions [row,column]
data['target'] = iris.target    # creating a new column
print(data.head())      # proof that new column is created
print(data[data.target == 1].head())
print(data[data.target == 2].head())
# 150 training samples, first 50 are setosa, then 50-100 versicolor, then rest 100-150 virginica
# so we split them all
setosa = data[:50]
versicolor = data[50:100]
virginica = data[100:]

# plotting a scatter graph against setosa and versicolor
# plt.xlabel('Sepal Length')
# plt.ylabel('Sepal Width')
# plt.scatter(setosa['sepal length (cm)'], setosa['sepal width (cm)'], color='red', marker='*')
# plt.scatter(versicolor['sepal length (cm)'], versicolor['sepal width (cm)'], color='blue', marker='.')
# plt.show()

# time to split test train
X1 = data.drop(['target'], axis='columns')
Y1 = data.target
x_train, x_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.2, random_state=1)
print(len(x_train))
print(len(x_test))


# creating a knn classifier
# minkowski is euclidean distance
knn = kncls(n_neighbors=10) # arguement is the K value
knn.fit(x_train, y_train)
print("Test with k=10: ", knn.score(x_test, y_test))

y_pred = knn.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)       # diagonals correct prediction, not on diagonal is wrong prediction
# sum of all values wil equate to sample data , here it is 30

print(classification_report(y_test, y_pred))