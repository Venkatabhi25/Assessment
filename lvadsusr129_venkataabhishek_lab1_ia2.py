# -*- coding: utf-8 -*-
"""LVADSUSR129_VENKATAABHISHEK_LAB1_IA2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DPLuzrPGl8TZKnYSMrP7I4iOx-e_J_o_
"""

import pandas as pd
df=pd.read_csv('/content/winequality-red.csv')
df.head()
df.info()

df.isnull().sum()
df.describe()

k=df['fixed acidity'].mean()
df.fillna(k)
k1=df['volatile acidity'].mean()
df.fillna(k1)
k2=df['citric acid'].mean()
df.fillna(k2)
k3=df['residual sugar'].mean()
df.fillna(k3)
k4=df['chlorides'].mean()
df.fillna(k4)
k5=df['free sulfur dioxide'].mean()
df.fillna(k5)
k6=df['sulphates'].mean()
df.fillna(k6)

if df['quality']>=3 and df['quality']<=6:
  df['quality']=0
elif df['quality']>=7 and df['quality']<=8:
  df['quality']=1

from scipy.stats import zscore
z_score = zscore(df)
print(z_score)

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

import warnings
warnings.filterwarnings("ignore")
correl=df.corr()
import matplotlib.pyplot as plt
plt.boxplot(correl)
plt.show()

import numpy as np
z_scores = zscore(df)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
df_clean = df[filtered_entries]
df.shape

X=df.iloc[:,1:]
y=df.iloc[:,0]
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(X,y,test_size=0.3,random_state=555)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(train_x, train_y)
y_pred = model.predict(test_x)

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
msne = mean_squared_error(test_y, y_pred)
print(msne)
sq_rt=np.sqrt(msne)
print(sq_rt)

r_2 = r2_score(test_y,y_pred)
print(r_2)
accuracy = accuracy_score(y_pred,test_y)