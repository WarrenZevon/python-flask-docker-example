import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import pickle


# Generate dummy dataset
np.random.seed(4)
dataset_size = 100


# Red points will be in the lower left corner, blue in the upper right
red = np.random.rand(dataset_size,2)*np.random.rand(dataset_size,2)
blue = 1-(np.random.rand(dataset_size,2)*np.random.rand(dataset_size,2))

X = np.concatenate([red,blue])
# Encode red as 0, blue as 1
labels = ['red','blue']
y = np.concatenate([np.zeros(dataset_size),np.ones(dataset_size)])


# Plot the data
plt.scatter(X[:,0],X[:,1], c=['red' if x==0 else 'blue' for x in y])
plt.show()


# Define model identifier and type
classifiers = [
      ('NeuralNetwork', MLPClassifier(alpha=.01, max_iter=500)),
      ('KNeighbor',  KNeighborsClassifier(2)),
      ('NaiveGaussian', GaussianNB())]

# Train and save models
for name, clf in classifiers:
    clf.fit(X, y)
    pickle.dump(clf, open('./models/'+name+'.pkl', 'wb'))


# Make a new prediction for point (0.9, 0.8) with the NeuralNetwork model
(model_name, model) = classifiers[0]

# Return an array of predictions so don't forget [0] at the end
prediction = model.predict(np.array([[0.9, 0.8]]))[0]
prediction_text = labels[int(prediction)]
print(f"The new point has been classified as {prediction} which decodes to {prediction_text}.")

