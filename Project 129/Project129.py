import csv

d1 = []
d2 = []

# Reading the files
with open('bright_stars.csv') as b:
    reader = csv.reader(b)
    for i in reader:
        d1.append(i)
    
with open('Dwarf_Stars.csv') as d:
    reader = csv.reader(d)   
    for i in reader:
        d2.append(i)

# Headers of both the files
h1 = d1[0]
h2 = d2[0]

# Stars data from both the files
sd1 = d1[1:]
sd2 = d2[1:]

starsData = []
head = h1 + h2

# Merging the data 
for i, data in enumerate(sd1):
    starsData.append(sd1[i] + sd2[i])

# Creating the final CSV file
with open('Merged_Stars_Data.csv', 'a+') as f:
    writer = csv.writer(f)
    writer.writerow(head)
    writer.writerows(starsData)
    