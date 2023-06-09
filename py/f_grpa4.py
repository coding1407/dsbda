# -*- coding: utf-8 -*-
"""F_GRPA4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WTr8CAde5y23hURjGKItqg2Eqtoq-6_3

#Data Analytics I
Create a Linear Regression Model using Python/R to predict home prices using Boston Housing 
Dataset (https://www.kaggle.com/c/boston-housing). The Boston Housing dataset contains 
information about various houses in Boston through different parameters. There are 506 samples 
and 14 feature variables in this dataset. 
The objective is to predict the value of prices of the house using the given features
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("HousingData.csv")

df.shape

df.head()

df.describe()

df.value_counts()

df.isnull().sum()

df.fillna(df.mean(),inplace=True)

df.isnull().sum()

sns.boxplot(df)

df.info()

plt.figure(figsize=(12,8))
sns.boxplot(df)

