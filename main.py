import pandas as pd

df = pd.read_csv('components.csv',index_col='index')
print(df.head())