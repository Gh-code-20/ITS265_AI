# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:30:28 2021

@author: Ghadir

Question 4: Create a neural network in Python and SKLearn using MLPRegressor (produces continuous 
output). The purpose of the neural network program is to predict real estate value based on the input data. 
Use the provided real-estate dataset in csv format. Create an input dataset from columns 2 – 6 
corresponding to the input feature set and an output dataset corresponding to the corresponding real estate 
prices (last column in the dataset). Use Sklearn train_test_split function to create the training and test 
datasets.
Configure the MLPRegressor neural network as follows:
• Input layer having 5 inputs.
• 2 hidden layers each with 100 nodes (Hint: in the nn parameters use (100,100) to 
represent it).
• Use the “relu” activation function
• Use the “adam” solver
• Set a learning rate of 0.001
• Number of epochs = 300
• Loss/cost function = mean spared error (MSE)
Train the neural network with the training set and then use then test it using the test input dataset.
Print out the mean square error and absolute error
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split



data= pd.read_csv("Real estate valuation data set.csv")
#print(data)

x = data.drop(['No', 'Y house price of unit area'], axis=1).values
y = data['Y house price of unit area'].values

# x = data.iloc[2:, :7]
# y = data.iloc[:,7]

print("X=\n",x)
print("Y=\n",y)


x_train, x_test, y_train, y_test = train_test_split(x, y)
                                                    
regr = MLPRegressor(hidden_layer_sizes=(100, 100),
                    activation='relu',
                     alpha=1e-4,
                    solver='adam',
                     tol=1e-4,
                    learning_rate_init=0.001,
                    max_iter=300,
                    random_state=1,
                    verbose=True)

regr.fit(x_train, y_train)
pred = regr.predict(x_test)
print(pred)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test,pred)
print("MSE:\n", mse)


from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test,pred)
print("MAE:\n", mae)



























# import pandas as pd
# import numpy as np
# #import matplotlib.pyplot as plt
# from sklearn import datasets
# #from sklearn.neural_network import MLPRegressor
# from sklearn.datasets import make_regression
# from sklearn.neural_network import MLPClassifier
# from sklearn.model_selection import train_test_split

# dataset= pd.read_csv("Real estate valuation data set.csv")
# print(dataset)

# X =dataset[dataset.iloc[2:6]]
# y =dataset['Price']

# # X_train = x[:1000]
# # Y_train = y[:1000]

# # x_test = x[1000:]
# # y_test = y[1000:]


# X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1)

# regr = MLPRegressor(hidden_layer_sizes=(2),solver='adam',
#                     learning_rate_init=0.001,
#                     max_iter=300,activation='relu',
#                     random_state=1, 
#                     max_iter=500).fit(X_train, y_train)


# pred=regr.predict(X_test[:2])

# regr.score(X_test, y_test)
# Calculating MSE:

# from sklearn.metrics import mean_squared_error
# mean_squared_error(y_test,pred)