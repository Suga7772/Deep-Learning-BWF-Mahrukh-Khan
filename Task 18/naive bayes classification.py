# ml algorithm , classification test , high dimensional data sets , sentimental analysis
# 'naive' because assumes ocurence of certain features that are independent to each other features
# bayes law, probability of event based on previous knowledge of the events
# P(A|B) = [ P(B|A) P(A) ] / P(B)
# Posterior probability = (likelihood). (Proposition prior probability) / [evidence prior probability or normalizing constant ]
# conditional theorem , reference : https://youtu.be/CPqOCI0ahss

# why naive? get  output based on the similiarity of outcomes ,believing that all independent variables are truly and fully independent
# - performs better moels assuming independnce, easy an fast precition
# categorical inputs aka numerical variables
# Cons :  zero frequency fail , its solution is laplace estimation
# known as bad estimator , independent predictor asumption ( in real life scenarios its highly unlikely it would ascertain)


from pydataset import data
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = data("DoctorAUS")        # 4 classes
X = data[['age', 'income', 'sex', 'illness', 'actdays', 'hscore', 'doctorco', 'nondocco', 'hospadmi', 'hospdays', 'medecine', 'prescrib']]
Y = data['insurance']       # independent variable
print(data)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# model training
cld = GaussianNB()
cld.fit(X_train, Y_train)

# model evaluation using classification
y_pred = cld.fit(X_train, Y_train).predict(X_test)
print(classification_report(Y_test, y_pred))        