import csv
import pandas as pd

df = pd.read_csv('Pro130.csv')
del df["Luminosity"]

df.dropna(axis = 1, inplace=True)

df = df.rename({'Star_name':'Bright Star Name'}, axis = 'columns')
df = df.rename({'Star_Name':'Dwarf Star Name'}, axis = 'columns')

print(df)

df.to_csv('FinalC130Project.csv')

