# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 00:56:54 2021

@author: Ghaidr
"""

from sklearn.cluster import KMeans
import pandas as pd
#import numpy as np
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt


df = pd.read_csv("IRIS.csv")
print(df[['petal_length','petal_width' ]])
print('Shape: ',df.shape)

plt.scatter(df['petal_length'],df['petal_width'])
plt.xlabel('petal_length')
plt.ylabel('petal_width')

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['petal_length','petal_width']])
#print(y_predicted)

df['cluster']=y_predicted
#print(df.head())

print("\nCluster Centeres:\n ", km.cluster_centers_)
#plt.plot(km.cluster_centers_)

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.petal_length,df1['petal_width'],color='green')
plt.scatter(df2.petal_length,df2['petal_width'],color='purple')
plt.scatter(df3.petal_length,df3['petal_width'],color='black')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='red',
            marker='*',label='centroid')
plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.legend()

# scal both
scaler = MinMaxScaler() #scaler object
scaler.fit(df[['petal_width']])  # Scales 0 to 1
df['petal_width'] = scaler.transform(df[['petal_width']])

scaler.fit(df[['petal_length']])
df['petal_length'] = scaler.transform(df[['petal_length']])
df.head()

plt.scatter(df.petal_length,df['petal_width'])


km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['petal_length','petal_width']])
y_predicted

df['cluster']=y_predicted
df.head()
print("\nCentroids after scaling:\n ",km.cluster_centers_)


df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.petal_length,df1['petal_width'],color='orange')
plt.scatter(df2.petal_length,df2['petal_width'],color='blue')
plt.scatter(df3.petal_length,df3['petal_width'],color='brown')

plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],
            color='pink',marker='*',
            label='centroid after scalling')
plt.legend()


sse = []
k_rng = range(1,15)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['petal_length','petal_width']])
    sse.append(km.inertia_)
        #sum(np.min(csse(df[['petal_length','petal_width']], 
                          #     km.cluster_centers_,'euclidean'),axis=1)) / (df[['petal_length','petal_width']].shape[0])
               
    

plt.xlabel('petal_length')
plt.ylabel('petal_width')
plt.plot(k_rng,sse)

# clf2 = KMeans(n_clusters=3, random_state=0).fit(df[['petal_length','petal_width']])
# print('Centroids of the clusters formed are:\n ', clf2.cluster_centers_)

   