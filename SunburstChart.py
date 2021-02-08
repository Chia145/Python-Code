import plotly.express as px
import pandas as pd 
""" Covid data
df = pd.read_csv("cd.csv")
fig = px.sunburst(df, path=['date', 'cases', 'country'], values='cases', color='country')
fig.show()"""


# random data
df = pd.read_csv("data2.csv")
fig = px.sunburst(df, path=['vendors', 'sectors', 'regions', 'sales'], values='sales', color='vendors')
fig.show()


""" My data:
vendors,sectors,regions,sales
0,A,Tech,North,1
1,B,Tech,North,3
2,C,Finance,North,2
3,D,Finance,North,4
4,None,Other,North,1
5,E,Tech,South,2
6,F,Tech,South,2
7,G,Finance,South,1
8,H,Finance,South,4
9,None,Other,South,1 """