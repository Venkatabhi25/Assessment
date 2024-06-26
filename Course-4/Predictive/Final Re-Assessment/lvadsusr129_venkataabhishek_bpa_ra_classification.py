# -*- coding: utf-8 -*-
"""LVADSUSR129_VENKATAABHISHEK_BPA_RA_CLASSIFICATION

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ny-iOX87wRYQaOgizXqS4VHwJ-nGD-Wi
"""

import pandas as pd
df=pd.read_csv('/content/penguins_classification.csv')
df.head()

df.describe()

df.info()

df.isnull().sum()
#there are 8 null values in bill_depth_mm column

df.drop_duplicates()

df=df.fillna(method='ffill')
df.isnull().sum()
#filling null values using forwad fill method in fillna

encoder = LabelEncoder()
df['species'] = encoder.fit_transform(df['species'])
df['island'] = encoder.fit_transform(df['island'])
df['year'] = encoder.fit_transform(df['year'])
df.head()

from matplotlib import pyplot as plt
df['bill_length_mm'].plot(kind='hist', bins=20, title='bill_length_mm')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='bill_length_mm', y='bill_depth_mm', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

x = df.drop(['species'], axis = 1)
y = df['species']
minmax = MinMaxScaler()

for i in x.columns:
  minmax.fit(x[[i]])
  x[i] = minmax.transform(x[[i]])

x.head()

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

model = RandomForestClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Accuracy score :", accuracy_score(y_test, y_pred)*100 )
print("Precision score :", precision_score(y_test, y_pred) )
print("Recall score :", recall_score(y_test, y_pred) )
print("F1 score :", f1_score(y_test, y_pred) )

matrix = confusion_matrix(y_test, y_pred)
print(matrix)

from xgboost import XGBClassifier
import math

xg_model = XGBClassifier()
xg_model.fit(x_train, y_train)
y_pred = xg_model.predict(x_test)

print("Using XGBoost Classifier : ")
print("Accuracy score :", accuracy_score(y_test, y_pred)*100 )
print("Precision score :", precision_score(y_test, y_pred) )
print("Recall score :", recall_score(y_test, y_pred) )
print("F1 score :", f1_score(y_test, y_pred) )

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Using Decision Tree Classifier : ")
print("Accuracy score :", accuracy_score(y_test, y_pred)*100 )
print("Precision score :", precision_score(y_test, y_pred) )
print("Recall score :", recall_score(y_test, y_pred) )
print("F1 score :", f1_score(y_test, y_pred) )