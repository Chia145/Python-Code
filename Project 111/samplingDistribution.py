import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
# C means Complete
Cmean = statistics.mean(data)
Cmedian = statistics.median(data)
Cmode = statistics.mode(data)
sd = statistics.stdev(data)

def RandomSetOfMeans(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    sampleMean = statistics.mean(dataset)
    return sampleMean

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans = RandomSetOfMeans(30)
        meanList.append(setOfMeans)


#calculating the Standard Deviations 1,2,3.
sd1Start = sampleMean - sd
sd1End = sampleMean + sd

sd2Start = sampleMean - (sd*2)
sd2End = sampleMean + (sd*2)

sd3Start = sampleMean - (sd*3)
sd3End = sampleMean + (sd*3)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sampleMean, sampleMean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[sd2Start, sd2End], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[sd3Start, sd3End], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()
