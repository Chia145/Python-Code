
import pandas as pd 
import plotly.express as px

df = pd.read_csv("cd.csv")
fig = px.scatter(df, x = 'date', y = 'cases', color = 'country', size = 'cases', size_max = 40)
fig.show()
