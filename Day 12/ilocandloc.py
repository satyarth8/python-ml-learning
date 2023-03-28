import pandas as pd
df=pd.read_csv('drink.csv')
df1=df.set_index('country')
df2=df1.loc[['India','Australia']]
df1.iloc[5,:]
df3=pd.read_csv('salary_Data.csv')
df3.sort_values(by=['exp','salary'])

