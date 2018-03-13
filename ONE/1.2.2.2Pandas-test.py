# -*- coding: UTF-8 -*-

import os
import pandas as pd
import requests

PATH = r'd:/pycharmWorkspace/ML/ONE/iris/'

r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

with open(PATH + 'iris.data', 'w') as f:
    f.write(r.text)

os.chdir(PATH)

df = pd.read_csv(PATH + 'iris.data', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

print('print(df.head())-------------------------------')
print(df.head())
print("print(df['sepal length'])-----------------")
print(df['sepal length'])
print('print(df.ix[:3,:2])----------------------------')
print(df.ix[:3,:2])
print("print(df.ix[:3, [x for x in df.columns if 'width' in  x]])--------------------")
print(df.ix[:3, [x for x in df.columns if 'width' in  x]])
print("print(df['class'].unique())")
print(df['class'].unique())
print("print(df[df['class']=='Iris-virginica'])----------------")
print(df[df['class']=='Iris-virginica'])
print("print(df.count())")
print(df.count())
print("print(df[df['class']=='Iris-virginica'].count())")
print(df[df['class']=='Iris-virginica'].count())

