import csv

articles = [] 
with open('articles.csv') as f:
    r = csv.reader(f)
    data = list(r)
    articles = data[1:]

liked = []
notLiked = []
