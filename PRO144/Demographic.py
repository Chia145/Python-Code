# import numpy as np
import csv
with open('articles.csv') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    column = data[0]

data = data.sort_values('totalEvents', ascending = False)

output = []
for data in data.head(20).values:
    column = data.columns
    output.append(dict(zip(column, data)))