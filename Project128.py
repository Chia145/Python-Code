from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(url)

soup = bs(page.text, 'html.parser')

starTable = soup.find_all('table')
# print(len(starTable)) 

tempList = []
tableRows = starTable[2].find_all

for r in tableRows:
    td = r.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)
print(tempList)

Star_Names = []
Distance = []
Mass = []
Radius = []

for i in range(1, len(tempList)):
    Star_Names.append(tempList[i][0])
    Distance.append(tempList[i][5])
    Mass.append(tempList[i][7])
    Radius.append(tempList[i][8])

header = ['Star_name','Distance','Mass','Radius']
df2 = pd.DataFrame(list(Star_Names, Distance, Mass, Radius),columns = header)
df2.to_csv('DwarfStars.csv')