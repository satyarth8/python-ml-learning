# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 15:42:07 2023

@author: Binod kumar
"""

import pandas as pd
df=pd.read_csv('Data.csv')
x=df.iloc[:,:3].values

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
x[:0]=le.fit_transform(x[:,0])
ley=LabelEncoder()
y[:0]=ley.fit_transform(x[:,0])

from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy='mean')
si=si.fit(x[:,1:3])
x[:,1:3]=si.transform(x[:,1:3])

from sklearn.model_selection import train_test_split