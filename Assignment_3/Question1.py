import pandas as panda
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
#Train Data
train_dt=panda.read_csv("./train.csv")
#Test Data
test_dt=panda.read_csv("./test.csv")
#Sex and Embarked with numerical values are replacing
train_dt['Sex'] = train_dt['Sex'].replace(["female", "male"], [0, 1])
train_dt['Embarked'] = train_dt['Embarked'].replace(['S', 'C', 'Q'], [1, 2, 3])
matrix = train_dt.corr()
print(matrix)
#showing the correlation between variables by heatmap
sb.heatmap(matrix, annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
plt.show()
sb.histplot(data=train_dt, x="Survived", hue="Sex")
plt.show()
classifier=GaussianNB()
train_dt.dropna(axis=0,inplace=True)
test_dt['Sex'] = train_dt['Sex'].replace(["female", "male"], [0, 1])
test_dt['Embarked'] = train_dt['Embarked'].replace(['S', 'C', 'Q'], [1, 2, 3])
test_dt.dropna(axis=0,inplace=True)
x=train_dt.loc[:,['Age', 'Embarked', 'Fare', 'Parch', 'Sex', 'SibSp']]
y=train_dt['Survived']
x_test=test_dt.loc[:,['Age', 'Embarked', 'Fare', 'Parch', 'Sex', 'SibSp']]
y_test=test_dt
from sklearn.metrics import accuracy_score
classifier.fit(x,y)
y_pred=classifier.predict(x_test)
print('accuracy is',accuracy_score(y[:13], y_pred))