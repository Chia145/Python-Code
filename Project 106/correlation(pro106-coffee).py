import csv 
import numpy
import plotly.express as px

def plot(dataPath):
    with open(dataPath) as csvfile: 
        df = csv.DictReader(csvfile)
        fig = px.scatter(df, x = "Coffee", y = "Sleep")
        fig.show()

def getData(dataPath):
    coffee = []
    sleep = []
    with open(dataPath) as csvfile: 
        df = csv.DictReader(csvfile)
        for row in df:
            coffee.append(float(row['Coffee']))
            sleep.append(float(row['Sleep']))
    return{"x": coffee, "y": sleep}

def find(source):
    correlation = numpy.corrcoef(source['x'],source['y'])
    print('Correlation between Coffee VS Sleep\n',correlation[0,1])
    
def main():
    path = 'coffee.csv'
    dataSource = getData(path)
    find(dataSource)
    plot(path)
    
main()    

