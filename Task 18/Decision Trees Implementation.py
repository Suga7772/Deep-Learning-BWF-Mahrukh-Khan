from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
print(clf.predict([[2., 2.]]))      # [1]

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
X, y = iris.data, iris.target
clfa = tree.DecisionTreeClassifier()
clfa = clf.fit(X, y)
tree.plot_tree(clfa)

import graphviz
dot_data = tree.export_graphviz(clfa, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")

plt.show()