# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:35:51 2021

@author: Ghadir
Problem 3: Import from SKLearn the handwritten digits dataset with 70000 examples.

Use “import fetch_openml” and the "mnist_784" dataset. 

Train the data on two different classifiers – Gaussian Naive Bayes Classifier and a Decision Tree Classifier. 

Compare the results and explain why one classifier is better at doing this classification than the other. 
Also, display a random set of 20 digit images.
 
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import datasets



#mnist = pd.read_csv("mnist_784.csv")
#mnist = fetch_openml(name="mnist_784")

mnist = fetch_openml("mnist_784", version=1)
print("Data=\n", mnist.data)
print("\nData shape",mnist.data.shape)
#print(mnist.target.shape)
#print(mnist)

#print(mnist.target)
#print(mnist.data)

X = mnist['data']
Y = mnist['target']

# digits = datasets.load_digits()
# print(digits.images[20])

                                                   
# split data into training and test sets

train_X, test_X, train_Y, test_Y = train_test_split(X, Y,
                                                    test_size=0.2, 
                                                    random_state=4)

# Classifier = cls
# Use Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
cls = MultinomialNB()
cls.fit(train_X, train_Y)

# score
print("\nNaive Bayes Score= " , cls.score(test_X, test_Y))

#Score How well did it classif each digit 0-9

from sklearn.metrics import classification_report
predictions = cls.predict(test_X)
print("\nClassification Results using Naive-Bayes Classifier\n")
print(classification_report(test_Y, predictions))

#Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
cls = DecisionTreeClassifier()
cls.fit(train_X, train_Y)

# score
print("\nDecision Tree Score= " , cls.score(test_X, test_Y))

#Score How well did it classif each digit 0-9
from sklearn.metrics import classification_report
predictions = cls.predict(test_X)
print("\nClassification Results using Decision Tree Classifier\n")
print(classification_report(test_Y, predictions))

#display a random set of 20 digit images.
digits_ds = load_digits()

fig, axes = plt.subplots(10,10, figsize=(8,8),
                          subplot_kw={'xticks':[], 'yticks':[]}, #x and y not corss the image
                          gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits_ds.images[i], cmap='binary', 
              interpolation = 'nearest')
    ax.text(0.05,0.05, str(digits_ds.target[i]),
            transform=ax.transAxes, color='green')
    
p = np.random.permutation(len(X))
p = p[:20]



# fig, axes = plt.subplots(7, 10, figsize=(10,10))
# for i, ax in enumerate(axes.flatten()):
#     ax.imshow(mnist[i].reshape((28,28)))
#     plt.setp(ax, xticks=[], yticks=[])
# plt.tight_layout()

# mnist_x, mnist_y = mnist[:, 1:], mnist[:,0] # separate target from pixels
# print(mnist_x.shape, mnist_y.shape)

# nfigs = 5
# fig = plt.figure(figsize=(10,10))
# for i in range(nfigs ** 2):
#     ax = fig.add_subplot(nfigs, nfigs, i+1)
#     ax.imshow(mnist_x[i].reshape(28, 28))








