# -*- coding: UTF-8 -*-
import seaborn as sns

import os
import pandas as pd
import requests

PATH = r'd:/pycharmWorkspace/ML/ONE/iris/'

os.chdir(PATH)

df = pd.read_csv(PATH + 'iris.data', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
#picture 1-23
sns.pairplot(df, hue = 'class')

# picture 1-24
fig, ax = plt.subplots(2, 2, figsize = (7, 7))
sns.set(style = 'white', palette = 'muted')
sns.violinplot(x = df['class'], y=df['sepal length'], ax = ax[0,0])
sns.violinplot(x = df['class'], y = df['sepal width'], ax = ax[0,1])
sns.violinplot(x = df['class'], y = df['petal length'], ax = ax[1,0])
sns.violinplot(x = df['class'], y = df['petal width'], ax = ax[1,1])
for i in  ax.flat:
    plt.setp(i.get_xticklabels(), rotation = 90)
fig.tight_layout()
plt.show()