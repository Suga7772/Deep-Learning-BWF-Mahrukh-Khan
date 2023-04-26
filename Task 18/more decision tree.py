import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
print(iris)
print(iris.data)

import seaborn as sns
df = sns.load_dataset('iris')
print(df.head)

X = df.iloc[:, :-1]     # species non independent feature
Y = iris.target

print(X)
print(Y)

# model training
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

print(X_train)

# making decision tree model
from sklearn.tree import DecisionTreeClassifier
treemodel = DecisionTreeClassifier()    # post pruning
treemodel.fit(X_train, Y_train)

from sklearn import tree
plt.figure(figsize=(10, 8))
tree.plot_tree(treemodel, filled=True)
# plt.show()

# prediction tyme
y_pred = treemodel.predict(X_test)
print(y_pred)

from sklearn.metrics import accuracy_score, classification_report
score = accuracy_score(y_pred, Y_test)
print(score)        # won't be good as we have not done any pruning

print(classification_report(y_pred, Y_test))
