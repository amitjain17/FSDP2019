# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:39:27 2019

@author: NITS
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("deliveryfleet.csv")
features = dataset.iloc[:,1:].values
#plt.scatter(features[:,0],features[:,1])


from sklearn.cluster import KMeans

"""For checking the Maximum cluster we want"""
#from sklearn.metrics import silhouette_score
#for n in range(2, 11):
#    clusterer = KMeans (n_clusters=n)
#    preds = clusterer.fit_predict(features)
#    centers = clusterer.cluster_centers_
#
#    score = silhouette_score (features, preds, metric='euclidean')
#    print("For n_clusters =", n, "The average silhouette_score is :", score)
#    
    
cluster = KMeans(n_clusters = 2,init = "k-means++",random_state=0)
pred = cluster.fit_predict(features)

plt.scatter(features[pred == 0,0],features[pred == 0,1],c='red',label = 'Cluster1')
plt.scatter(features[pred == 1,0],features[pred == 1,1],c='blue',label = 'Cluster2')
#plt.scatter(cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.legend()


cluster = KMeans(n_clusters = 4,init = "k-means++",random_state=0)
pred = cluster.fit_predict(features)

plt.scatter(features[pred == 0,0],features[pred == 0,1],c='purple',label = 'Cluster3')
plt.scatter(features[pred == 1,0],features[pred == 1,1],c='orange',label = 'Cluster4')
plt.scatter(cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.xlabel("Distance")
plt.ylabel("Speed")
plt.legend()