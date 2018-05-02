# -*- coding: UTF-8 -*-
import seaborn as sns

import os
import pandas as pd
import requests

PATH = r'd:/pycharmWorkspace/ML/ONE/iris/'

os.chdir(PATH)

df = pd.read_csv(PATH + 'iris.data', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

df['class'] = df['class'].map({'Iris-setosa':'SET', 'Iris-virginica':'VIR','Iris-versicolor':'VER'})
print(df)
