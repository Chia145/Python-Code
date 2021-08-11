import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('final.csv')
df = df[df['soup'].notna()]

count = CountVectorizer(stop_words = 'english')
count_matrix = count.fit_transform(df['soup']) 

cos = cosine_similarity(count_matrix, count_matrix)

df = df.reset_index()
indices = pd.Series(df.index, index = df['original_title'])

def recommend(t):
  i = indices[t]
  scores = list(enumerate(cos[i]))
  scores = sorted(scores, key = lambda x:x[1], reverse = True)
  scores = scores[1:11]
  movieIndices = [j[0] for j in scores]
  return df[['original_title', 'vote_count', 'vote_average', 'score', 'posterLink', 'release_date', 'runtime', 'overview']].iloc[movieIndices].value.tolist()

