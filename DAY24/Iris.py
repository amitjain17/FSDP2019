# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:01:50 2019

@author: NITS
"""
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
info = datasets.load_iris()

features = pd.DataFrame(info.data)
features.columns = info.feature_names

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
features = pca.fit_transform(features)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3 ,init='k-means++',random_state=0)
pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1],c = 'blue', label = 'setosa')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'virginica')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'versicolor')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'centroids')
plt.legend()
plt.show()