# -*- coding: UTF-8 -*-
import os
import pandas as pd
import requests

PATH = r'd:/pycharmWorkspace/ML/ONE/iris/'

os.chdir(PATH)

df = pd.read_csv(PATH + 'iris.data', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

import matplotlib.pyplot as plt
plt.style.use('ggplot')
#%matplotlib inline
import numpy as np

#picture 1-18
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df['petal width'], color = 'black')
ax.set_ylabel('Count', fontsize = 12)
ax.set_xlabel('Width', fontsize = 12)
plt.title('Iris Petal Width', fontsize = 14, y = 1.01)
plt.show()
#picture 1-19
fig, ax = plt.subplots(2, 2, figsize = (6, 4))

ax[0][0].hist(df['petal width'], color = 'blue')
ax[0][0].set_ylabel('Count', fontsize = 12)
ax[0][0].set_xlabel('Width', fontsize = 12)
ax[0][0].set_title('Iris Petal Width', fontsize = 14, y = 1.01)

ax[0][1].hist(df['petal length'], color = 'red')
ax[0][1].set_ylabel('Count', fontsize = 12)
ax[0][1].set_xlabel('Length', fontsize = 12)
ax[0][1].set_title('Iris Petal Lenth', fontsize = 14, y = 1.01)

ax[1][0].hist(df['sepal width'], color = 'blue')
ax[1][0].set_ylabel('Count', fontsize = 12)
ax[1][0].set_xlabel('Width', fontsize = 12)
ax[1][0].set_title('Iris Sepal Width', fontsize = 14, y = 1.01)

ax[1][1].hist(df['sepal length'], color = 'red')
ax[1][1].set_ylabel('Count', fontsize = 12)
ax[1][1].set_xlabel('Length', fontsize = 12)
ax[1][1].set_title('Iris Sepal Lenth', fontsize = 14, y = 1.01)

plt.tight_layout()
plt.show()

#picture 1-20
fix, ax = plt.subplots(figsize = (6, 6))
ax.scatter(df['petal width'], df['petal length'], color = 'green')
ax.set_xlabel('Petal Width')
ax.set_ylabel('Petal Length')
ax.set_title(r'Petal Scatterplot')
plt.show()

#picture 1-21
fig, ax = plt.subplots(figsize = (6,6))
ax.plot(df['petal length'], color = 'blue')
ax.set_xlabel('Specimen Number')
ax.set_ylabel('Petal Length')
ax.set_title('Petal Length Plot')
plt.show()

#picture 1-22
fig, ax = plt.subplots(figsize = (6,6))
bar_width = 0.8
labels = [x for x in df.columns if 'length' in x or 'width' in x]
ver_y = [df[df['class'] == 'Iris-versicolor'][x].mean() for x in labels]
vir_y = [df[df['class'] == 'Iris-virginica'][x].mean() for x in labels]
set_y = [df[df['class'] == 'Iris-setosa'][x].mean() for x in labels]
x = np.arange(len(labels))
ax.bar(x, vir_y, bar_width, bottom = set_y, color = 'darkgrey')
ax.bar(x, set_y, bar_width, bottom = ver_y, color = 'white')
ax.bar(x, ver_y, bar_width, color = 'black')
ax.set_xticks(x + (bar_width/2))
ax.set_xticklabels(labels, rotation = -70, fontsize = 20)
ax.set_title('Mean Feature Measurement By Class', y = 1.01)
ax.legend(['Virginica', 'Setosa', 'Versicolor'])
plt.show()