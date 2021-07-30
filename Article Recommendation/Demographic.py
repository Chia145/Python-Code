import numpy as np
import pandas as pd

df = pd.read_csv('articles.csv')

totalEvents = df.copy().loc[df['totalEvents']]
totalEvents = totalEvents.sort_values('totalEvents', ascending = False)
output = totalEvents[['title', 'lang', 'contentType', 'eventType']]
