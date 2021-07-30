import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('articles.csv')
df = df[df['title'].notna()]

count = CountVectorizer(stop_words = 'english')
countMatrix = count.fit_transform(df['title']) 

cos = cosine_similarity(countMatrix, countMatrix) 

# df = df.reset_index()
indices = pd.Series(df.index, index = df['contentId'])

def recommendArticle(title, cos):
  i = indices[title]
  s = list(enumerate(cos[i]))
  s = sorted(s, key = lambda x:x[1], reverse = True)
  s = s[1:7]
  articleIndices = [j[0] for j in s]
  return df['title'].iloc[articleIndices]