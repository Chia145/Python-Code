import pandas as pd 
import plotly.express as px
import statistics

df = pd.read_csv('appdata.csv')

#converting the data into list 
data = df['attempt'].tolist()

# finding the mean of the no. of attempts 
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
# print("The mean of the attempts is: ",mean)

# plotting the graph
graph = px.scatter(mean,x = 'student_id', y = 'level', color = 'attempt')
graph.show()
