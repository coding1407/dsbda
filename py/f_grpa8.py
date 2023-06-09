# -*- coding: utf-8 -*-
"""F_GRPA8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n_RgfWchR91nLsd9W9P67Xaw-HS08rdm

# Group A
Assignment No.8

Data Visualization 1
"""

import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset("titanic")

df.head()

df.info()

df['sex'].value_counts()

df.shape

df.isnull().sum()

df.describe()

df['embarked'].value_counts()

df['embarked'].fillna('S',inplace=True)

df.isnull().sum()

df['age'].fillna(df['age'].mean(),inplace=True)

df.isnull().sum()

df.fillna(method='ffill',inplace=True)

df.isnull().sum()

df.fillna(method='bfill',inplace=True)

df.isnull().sum()

sns.histplot(df['fare']) # to find the data distribution histogram is used

"""### EDA [Exploratory data analysis]

####  1.Univariate Analysis
Numerical ==> histplit(),kdeplot(),lineplot()[time series]
Categorical ==>
"""

sns.kdeplot(df['age'])

sns.displot(df['age'])

sns.boxplot(df['age'])

sns.distplot(df['age'])

sns.histplot(df["age"])

sns.kdeplot(df["fare"])

sns.histplot(df['fare'])

sns.boxplot(df['fare'])

sns.distplot(df['fare'])

Q1=df['age'].quantile(0.25)

Q3=df['age'].quantile(0.75)

IQR = Q3-Q1

lower = Q1 - (1.5*IQR)

upper = Q3 + (1.5*IQR)

np.clip(df['age'],lower,upper,inplace=True)

sns.boxplot(df['age'])

Q1 = df['fare'].quantile(0.25)

Q3=df['fare'].quantile(0.75)

IQR = Q3-Q1

lower = Q1 - (1.5*IQR)

upper = Q3 + (1.5*IQR)

np.clip(df['fare'],lower,upper,inplace=True)

sns.boxplot(df['fare'])

def outlier_treatment(df,col):
    Q1 = df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR = Q3-Q1
    lower = Q1 - (1.5*IQR)
    upper = Q3 + (1.5*IQR)
    np.clip(df[col],lower,upper,inplace=True)

outlier_treatment(df,'fare')

sns.boxplot(df['fare'])

outlier_treatment(df,'age')

sns.boxplot(df['age'])

"""Categorical ==> countplot, piechart()"""

sns.countplot(df['survived'])

sns.countplot(df['pclass'])

sns.countplot(df['sex'])

sns.countplot(df['sibsp'])

sns.countplot(df['parch'])

sns.countplot(df['embarked']) # we can plot count plot for all categorical values i.eclass          0
    who            0
    adult_male     0
    deck           0
    embark_town    0
    alive          0
    alone

df['survived'].value_counts().plot(kind='pie',autopct='%.2f%%')

df['survived'].value_counts().plot(kind='pie')

df['survived'].value_counts().plot(kind='pie',autopct='%.2f%%')

"""bivariate analysis
types

#(numerical numerical) scatterplot,pairplot
#(numerical categorical) barplot,boxplot,voilin-plot
#(categorical categorical) heat-map,cluster-map(use concept of crosstab)

28/04/23
"""

sns.scatterplot(x='age',y='fare',data=df)

sns.pairplot(data=df)

sns.boxplot(x='survived',y='age',data=df)
#75% people not survived are inbetween 30-40 age
#maximum not survived age is above 50 but we cannot conclude something out of it so plot barplot

sns.barplot(x='survived',y='age',data=df)

sns.barplot(x='survived',y='age',hue='sex',data=df)

sns.countplot(x='survived',hue='sex',data=df)

sns.barplot(x='class',y='fare',data=df)

sns.barplot(x='survived',y='fare',data=df)

#sns.distplot(x='survived',y='age',data=df)

pd.crosstab(df['sex'],df['survived'])
#crosstab creates new table which is called as contigency Table

sns.heatmap(pd.crosstab(df['sex'],df['survived']))

pd.crosstab(df['pclass'],df['survived'])

sns.heatmap(pd.crosstab(df['pclass'],df['survived']))

sns.clustermap(pd.crosstab(df['pclass'],df['survived']))

pd.crosstab(df['deck'],df['survived'])

sns.clustermap(pd.crosstab(df['deck'],df['survived']))

sns.voilinplot(pd.crosstab(df['deck'],df['survived'],data=df)