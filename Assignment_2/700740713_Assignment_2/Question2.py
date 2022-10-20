import pandas as panda

#1
data = panda.read_csv('data.csv')

#2
data.describe(include='all')
print(data)
#3
data.isnull().any()
print(data)
#3a
data2 = data.fillna(data.replace('',data.mean()))
data2['Calories'] = data2['Calories'].fillna(data2['Calories'].mean())
print(data2)

data2.isnull().any()

#4
data2.groupby(['Pulse']).agg({'Duration': ['min']}).reset_index()

data2.groupby(['Pulse']).agg({'Duration': ['max']}).reset_index()

data2.groupby(['Pulse']).agg({'Duration': ['count']}).reset_index()

data2.groupby(['Pulse']).agg({'Duration': ['mean']}).reset_index()

#5
data2[(data2['Calories'] > 500) & (data2['Calories'] < 1000)]

#6
data2[(data2['Calories'] > 500) | (data2['Calories'] < 100)]

#7
data_modified = data2.drop('Maxpulse', axis = 1)
data_modified

#8
data3 = data2.copy()
del data3['Maxpulse']
print(data3)

#9
print(data3.dtypes)

data3['Calories'] = data3['Calories'].astype(int)
print(data3.dtypes)

data3

#10
data3.plot.scatter(x='Duration', y='Calories', c='DarkBlue')
