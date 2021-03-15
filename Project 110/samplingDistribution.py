import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
fig.show()
pMean = statistics.mean(data)
print("Mean of the Population:- ",pMean)
def randomMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex= random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans= randomMean(10)
        meanList.append(setOfMeans)
    show_fig(meanList)
    sampleMean = statistics.mean(meanList)
    print("sampling mean:- ",sampleMean)
setup()