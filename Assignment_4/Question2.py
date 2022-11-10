import pandas as panda
import numpy as nump
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
desired_width=320
panda.set_option('display.width', desired_width)
panda.set_option('display.max_columns',20)
df2=panda.read_csv("./K-Mean_Dataset.csv")
print(df2.head())
X = df2.iloc[:,1:].values
imputer = SimpleImputer(missing_values=nump.nan, strategy='mean')
imputer = imputer.fit(X)
x = imputer.transform(X)
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
from sklearn.cluster import KMeans
nclusters = 2
km = KMeans(n_clusters=nclusters)
print(km.fit(x))
y_cluster_kmeans = km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, y_cluster_kmeans)
print('Silhouette score:',score)
