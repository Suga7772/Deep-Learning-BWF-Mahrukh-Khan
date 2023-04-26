import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("titanic.csv")
print(data.head(10))

# drop irrelevant vairables and leave behind the important variables
data.drop(['PassengerId', 'Name', 'SibSp', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)
print(data.head())

target = data.Survived
inputs = data.drop(['Survived'], axis='columns')

dummies = pd.get_dummies(inputs.Sex)
print(dummies.head(3))

# now concat the dummy columns
inputs = pd.concat([inputs, dummies], axis='columns')
print(inputs.head(4))

# drop male cus  dummy variable trap theory , one female gender bool is enoughn to deduce
inputs.drop(['Sex', 'male'], axis='columns', inplace=True)
print(inputs.head(4))

# checking if we have any missing/na values in any columns
print("\n\n", inputs.columns[inputs.isna().any()])

print(inputs.Age[:10], "\n\n")
# lettuce handle the Nan
# replacing the nan with a mean of all values
inputs.Age = inputs.Age.fillna(inputs.Age.mean())
print(inputs.head(5), "\n\n")

X_train, X_test, Y_train, Y_test = train_test_split(inputs, target, test_size=0.2)

# creating naive bayes model
# gaussian naive bayes when data distribution is normal
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))
print(X_test[:10])  # check first 10 x samples
print(Y_test[:10])  # check first 10 y samples

print(model.predict(X_test[:10]))
print(model.predict_proba(X_test[:10])) # sample with respect to each element of the persons survival