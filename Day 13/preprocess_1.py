# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:51:47 2023

@author: Binod kumar
"""
import pandas as pd
df = pd.DataFrame({'Name': ['John', 'Alice', 'Bob', 'Lisa'],'Age': [25, 30, 35, 40],'Country': ['USA', 'Canada', 'UK', 'Australia']})
first=df.iloc[1:3]
# find locates the column 
