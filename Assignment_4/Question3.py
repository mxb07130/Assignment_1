import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
df2=pd.read_csv("./K-Mean_Dataset.csv")
df2.head()
X = df2.iloc[:,1:].values
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(X)
x = imputer.transform(X)
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array)
from sklearn.cluster import KMeans
nclusters = 2
km = KMeans(n_clusters=nclusters)
km.fit(X_scaled)
y_scaled_cluster_kmeans = km.predict(X_scaled)
from sklearn import metrics
score = metrics.silhouette_score(X_scaled, y_scaled_cluster_kmeans)
print('Silhouette score after applying scaling:',score)
