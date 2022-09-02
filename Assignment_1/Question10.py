import numpy as np  #importing important python libraries
import matplotlib.pyplot as plt  
import pandas as pd
path=r"D:\ML\dataset .csv"
data=pd.read_csv(path)#reading the dataset
print(data)
x= data['Feature'].values
y= data['Class'].values
print(x,y)
#dividing data equally into training and testing data
from sklearn.model_selection import train_test_split  
features_tr, features_te, label_tr, label_te= train_test_split(x, y, random_state=0, train_size= 0.5 ) 
#reshaping the data feature and labes into 2D array
features_tr = np.array(features_tr).reshape(-1,1)
features_te = np.array(features_te).reshape(-1,1)
#Normalizing data
from sklearn.preprocessing import StandardScaler    
normalization= StandardScaler()    
features_tr= normalization.fit_transform(features_tr)    
features_te= normalization.transform(features_te)  
#fiting the training data into classifier model 
from sklearn.neighbors import KNeighborsClassifier  
model= KNeighborsClassifier(n_neighbors=3 )  
model.fit(features_tr, label_tr)
#Predicting the test set result  
predict_class= model.predict(features_te)  
print("Predicted Test Samples Output:",predict_class)

#creating a confusion matrix
from sklearn.metrics import confusion_matrix  
model_evaluation= confusion_matrix(label_te, predict_class) 
print("Confusion matrix:\n",model_evaluation)
#finding model accuracy
count=sum(sum(model_evaluation))
accuracy=(model_evaluation[0,0]+model_evaluation[1,1])/count
print ('Accuracy =: ', accuracy)
# finding model sensitivity
sense = model_evaluation[0,0]/(model_evaluation[0,0]+model_evaluation[0,1])
print('Sensitivity =: ', sense )
#finding model specificity
speci = model_evaluation[1,1]/(model_evaluation[1,0]+model_evaluation[1,1])
print('Specificity =: ', speci)