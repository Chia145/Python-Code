import pandas as pd 
import plotly.figure_factory as px
import statistics 
import plotly.graph_objects as go

# Finding mean, median mode and Standard deviation of the data.
df = pd.read_csv("StudentPerformance.csv")
data = df['math score'].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
sd = statistics.stdev(data)

print("Mean, Median, Mode and Standard deviation of the data is {}, {}, {} and {} respectively.".format(mean, median, mode, sd) )

#calculating the Standard Deviations 1,2,3.
sd1Start = mean - sd
sd1End = mean + sd

sd2Start = mean - (sd*2)
sd2End = mean + (sd*2)

sd3Start = mean - (sd*3)
sd3End = mean + (sd*3)

# Score within Standard deviations ('s' stands for score)
s1 = [r for r in data if r>sd1Start and r<sd1End]
s2 = [r for r in data if r>sd2Start and r<sd2End]
s3 = [r for r in data if r>sd3Start and r<sd3End]

print('{}% of the data lies between the first Standard deviation'.format(len(s1)*100.0/len(data)))
print('{}% of the data lies between the second Standard deviation'.format(len(s2)*100.0/len(data)))
print('{}% of the data lies between the third Standard deviation'.format(len(s3)*100.0/len(data)))

#Ploting the data
fig1 = px.create_distplot([df['math score'].tolist()],['Maths Score'],show_hist = False)
fig1.show()
"""fig2 = px.create_distplot([df['reading score'].tolist()],['Reading Score'],show_hist = False)
fig2.show()
fig3 = px.create_distplot([df['writing score'].tolist()],['Writing Score'],show_hist = False)
fig3.show()
"""