import pandas as pd
df1=pd.read_csv('income.csv')
print(df1.head())

print(df1.age_group.unique())

print(df1.groupby(df1.age_group).count())

print(df1.groupby(df1.age_group).min())

print(df1.groupby(df1.age_group).max())

print(df1.groupby(df1.age_group).mean())

print(df1.groupby(df1.age_group).std())

print(df1.groupby(df1.age_group).describe())

from sklearn import datasets

data=datasets.load_iris()
df=pd.DataFrame(data.data,columns=data.feature_names)
df['species']=pd.Series(data.target)
print(df.head())

print(df.species.unique())
    
print(df.groupby(df.species))

print(df.groupby(df.species).count())

print(df.groupby(df.species).max())

print(df.groupby(df.species).min())

print(df.groupby(df.species).mean())

print(df.groupby(df.species).std())

print(df.groupby(df.species)["sepal length (cm)"].describe())

print(df.groupby(df.species)["sepal width (cm)"].describe())

print(df.groupby(df.species)["petal length (cm)"].describe())

print(df.groupby(df.species)["petal width (cm)"].describe())
