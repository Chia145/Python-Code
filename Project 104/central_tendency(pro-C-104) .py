import csv 
with open ("HeightWeight.csv", newline='') as f: 
    r = csv.reader(f)
    data = list(r)

data.pop(0)

# Mean
newData = []
for i in range(len(data)):
    num = data[i][2]
    newData.append(float(num)) 

n = len(newData)

total = 0
for x in newData:
    total += x

mean = total/n
print('Mean or average is: '+ str(mean))


# Median
newData.sort()
 
if n % 2 == 0 :
    m1 = float(newData[n//2])
    m2 = float(newData[n//2 - 1]) 
    median = (m1 + m2)/2
else:
    median = newData[n//2]

print('Median is: '+ str(median))    


# Mode
from collections import Counter 

d = Counter(newData)
modeRange = {
    '75-95' : 0,
    '95-115' : 0,
    '115-135' : 0,
    '135-155' : 0,
    '155-175' : 0,
}

for h,o in d.items():
    if 75 < float(h) < 95:
        modeRange['75-95'] += o
    elif 95 < float(h) < 115:
        modeRange['95-115'] += o
    elif 115 < float(h) < 135:
        modeRange['115-135'] += o
    elif 135 < float(h) < 155:
        modeRange['135-155'] += o
    elif 155 < float(h) < 175:
        modeRange['155-175'] += o
# print(modeRange.items())

mode_occurance, m_range = 0,0 
for r,o in modeRange.items():
    if o > mode_occurance:
        m_range, mode_occurance = [int(r.split("-")[0]),int(r.split("-")[1])], o

mode = float((m_range[0] + m_range[1])/2) 
print("Mode is :", mode)
