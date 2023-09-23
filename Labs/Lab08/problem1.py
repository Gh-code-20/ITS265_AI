# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:10:51 2021

@author: Ghadir Alfadhl
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
#from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df= pd.read_csv("data-Lab10.csv")
print(df.head())

# Normalization in the range 1 to 3
def normalize(values, actual_bounds, desired_bounds):
    return [desired_bounds[0] + (x - actual_bounds[0]) * (desired_bounds[1] - desired_bounds[0]) / (actual_bounds[1] - actual_bounds[0]) 
            for x in values]

#normalized in the range of 1 and 3
for i in df.columns:
    df[i]= normalize(df[i], [min(list(df[i])), max(list(df[i]))], [1,3] )

print(df[i])
X= df[['ReT', 'In_v']]
y= df['Out_T']

# splitting the data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.5,
                                                    random_state=1)

# Implementing Lasso
from sklearn.linear_model import Lasso

model= Lasso(alpha= 0.01, normalize=True)
model = model.fit(X_train, y_train)

MSE = np.square(np.subtract(y_test, model.predict(X_test))).mean()
print("this is mse=\n", MSE)

# plotting the MSE vs learning rate
#Show your output and plot of mean MSEs of training and 
#validation for different learning rate values (alpha). 
#And you should conclude with your selection of learning rate value and
# explain why your selection optimizes the model.  

alpha=[]
mse=[]
i=0.01
while i<0.3:
    alpha.append(i)
    model= Lasso(alpha=i, normalize=True)
    model= model.fit(X_train, y_train)
    MSE= np.square(np.subtract(y_test, model.predict(X_test))).mean()
    mse.append(MSE)
    i += 0.01

print("this is model=", alpha)
plt.plot(alpha, mse)
plt.xlabel("Learning rate")
plt.ylabel("MSE")
plt.show()