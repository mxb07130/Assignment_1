import pandas as panda
import numpy as nump
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
desired_width=320
panda.set_option('display.width', desired_width)
panda.set_option('display.max_columns',20)
df2=panda.read_csv("./K-Mean_Dataset.csv")
X = df2.iloc[:,1:].values
imputer = SimpleImputer(missing_values=nump.nan, strategy='mean')
imputer = imputer.fit(X)
x = imputer.transform(X)
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = panda.DataFrame(X_scaled_array)
from sklearn.cluster import KMeans
nclusters = 2
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)
KMeans(n_clusters=2)

y_scaled_cluster_kmeans = km.predict(X_scaled)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_scaled_cluster_kmeans)
print('Silhouette score after applying scaling:',score)