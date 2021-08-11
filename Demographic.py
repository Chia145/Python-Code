import pandas as pd
import numpy as np
df = pd.read_csv('final.csv')

c = df["vote_average"].mean()
m = df['vote_count'].quantile(0.9)

movies = df.copy().loc[df['vote_count']>=m]

def weightedRating(x, m=m, c=c):
  v = x['vote_count']
  r = x['vote_average']
  wr = (v/(v+m)*r) + (m/(v+m)*c)
  return wr

movies['score'] = movies.apply(weightedRating, axis = 1)
movies = movies.sort_values('score', ascending = False)
output = movies[['original_title', 'vote_count', 'vote_average', 'score', 'posterLink', 'release_date', 'runtime', 'overview']].head(20).values.tolist()