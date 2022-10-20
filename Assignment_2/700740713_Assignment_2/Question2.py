import pandas as pd

#1
df = pd.read_csv('./data.csv')
df

#2
df.describe(include='all')

#3
df.isnull().any()

#3a
df2 = df.fillna(df.replace('',df.mean()))
df2['Calories'] = df2['Calories'].fillna(df2['Calories'].mean())
df2

df2.isnull().any()

#4
df2.groupby(['Pulse']).agg({'Duration': ['min']}).reset_index()

df2.groupby(['Pulse']).agg({'Duration': ['max']}).reset_index()

df2.groupby(['Pulse']).agg({'Duration': ['count']}).reset_index()

df2.groupby(['Pulse']).agg({'Duration': ['mean']}).reset_index()

#5
df2[(df2['Calories'] > 500) & (df2['Calories'] < 1000)]

#6
df2[(df2['Calories'] > 500) | (df2['Calories'] < 100)]

#7
print(df2)
df_modified = df2.drop('Maxpulse', axis = 1)
df_modified

#8
df3 = df2.copy()
del df3['Maxpulse']
df3

#9
print(df3.dtypes)

df3['Calories'] = df3['Calories'].astype(int)
print(df3.dtypes)

df3
#10
df3.plot.scatter(x='Duration', y='Calories', c='DarkBlue')


plot.show()