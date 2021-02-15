
import math 
import csv 
with open ("data(105).csv", newline='') as f: 
    r = csv.reader(f)
    fileData = list(r)

data = fileData[0]

n = len(data)
total = 0
for x in data:
    total += int(x)

mean = total/n

squaredList = []
for num in data:
    a = int(num)-mean
    a = a**2  
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum += i

result = sum/(n-1)

sd = math.sqrt(result) 

print('Mean:', mean)
print('Standard deviation: ', sd)


