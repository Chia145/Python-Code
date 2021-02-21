import csv 
import numpy
import plotly.express as px
def plot(dataPath):
    with open(dataPath) as csvfile: 
        df = csv.DictReader(csvfile)
        fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present")
        fig.show()

def getData(dataPath):
    marks = []
    days = []
    with open(dataPath) as csvfile: 
        df = csv.DictReader(csvfile)
        for row in df:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    return{"x": marks, "y": days}

def find(source):
    correlation = numpy.corrcoef(source['x'],source['y'])
    print('Correlation between Marks VS Days Present\n',correlation[0,1])

def main():
    path = 'student.csv'
    dataSource = getData(path)
    find(dataSource)
    plot(path)

main()
