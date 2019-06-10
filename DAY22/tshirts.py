# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:25:53 2019

@author: NITS
"""
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("tshirts.csv")
features = dataset.iloc[:,1:].values
#plt.scatter(features[:,0],features[:,1])

from sklearn.cluster import KMeans

"""Check the how many cluster we have to required"""
#from  sklearn.metrics import silhouette_score
#for n in range(2,11):
#    clus = KMeans(n_clusters = n)
#    pred = clus.fit_predict(features)
#    score = silhouette_score(features,pred,metric = 'euclidean')
#    print("For n_clusters =", n, "The average silhouette_score is :", score)


cluster1 = KMeans(n_clusters= 3,init= "k-means++",random_state=0)
pred1 = cluster1.fit_predict(features)
plt.scatter(features[pred1==0, 0],features[pred1==0, 1],c='red',label = 'Medium')
plt.scatter(features[pred1==1, 0],features[pred1==1, 1],c='purple',label = 'Large')
plt.scatter(features[pred1==2, 0],features[pred1==2, 1],c='blue',label = 'Small')
plt.scatter(cluster1.cluster_centers_[:,0],cluster1.cluster_centers_[:,1],c='yellow',label='centroids')
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()

print("Small_Person_Height:",cluster1.cluster_centers_[2,0],"Small_Person_Weight:",cluster1.cluster_centers_[2,1])
print("Medium_Person_Height:",cluster1.cluster_centers_[0,0],"Small_Person_Weight:",cluster1.cluster_centers_[0,1])
print("Large_Person_Height:",cluster1.cluster_centers_[1,0],"Small_Person_Weight:",cluster1.cluster_centers_[1,1])

