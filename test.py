import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
from matplotlib import style


data = pd.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"
X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

best = 0
# for _ in range(1000):
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
#     linear = linear_model.LinearRegression()
#     linear.fit(x_train, y_train)
#     acc = linear.score(x_test, y_test)
#     if acc > best:
#         print(acc)
#         best = acc
#         with open("studentmodel.pickle", "wb") as f:
#             pickle.dump(linear, f)

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(x_test)

for x in range (len(predictions)):
    print(predictions[x], x_test[x], y_test[x])


