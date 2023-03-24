# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 10:42:56 2023

@author: Saatyrth
"""

import pandas as pd
data=list(range(1,11))
df=pd.Series(data)
ol=[]
z=0
h=df.mean()
sd=int(df.std())
for x in data:
    z= int((x-h)/sd)
    if(z<=-3 or z>=3):
        ol.append(x)
print(ol)
    