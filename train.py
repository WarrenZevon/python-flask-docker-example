import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import pickle


# Generate dummy dataset
np.random.seed(4)

dataset_size = 100

# reds will be in the lower left corner, blue in the upper right
red = np.random.rand(dataset_size,2)*np.random.rand(dataset_size,2)
blue = 1-(np.random.rand(dataset_size,2)*np.random.rand(dataset_size,2))

X = np.concatenate([red,blue])
# encode red as 0, blue as 1
y = np.concatenate([np.zeros(dataset_size),np.ones(dataset_size)])


plt.scatter(X[:,0],X[:,1], c=['red' if x==0 else 'blue' for x in y])
plt.show()


classifiers = [
      ('NeuralNetwork', MLPClassifier(alpha=.01, max_iter=500)),
      ('DecisionTree', DecisionTreeClassifier(max_depth=5)),
      ('NaiveGuassian', GaussianNB())]

for name, clf in classifiers:
    clf.fit(X, y)
    print(name, clf.score(X,y))
    pickle.dump(clf, open('./models/'+name+'.pkl', 'wb'))

