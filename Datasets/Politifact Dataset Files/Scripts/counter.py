import pandas as pd
import random
import codecs
from collections import Counter

csv = pd.read_csv('Poems.csv', sep=';')
print(csv)
lista = []
counter =[]
tags=[]

'''
for row in csv["tags"]:
    row = row.replace('[','').replace(']','').replace("'",'')
    row = row.split(",")
    for tag in row:
        tag_f = tag.replace(' ','')
        
        if tag_f not in lista:
            tags.append(tag_f)
    
        lista.append(tag_f)
'''

'''
items = lista
for tag in tags:
    counts = Counter(items)
    count = counts[tag]
    counter.append(tag + ': ' + str(count))
'''

def summary_length(summary):
    summary = str(summary)
    #summary = summary.replace('\n', ' ')
    #tokens = summary.split(' ')
    return len(summary)

            
csv["summaryLength"] = csv.apply(lambda row: summary_length(row["summary"]), axis=1)
csv["claimLength"] = csv.apply(lambda row: summary_length(row["claim"]), axis=1)
csv["poemsLength"] = csv.apply(lambda row: summary_length(row["poems"]), axis=1)
csv["labelLength"] = csv.apply(lambda row: summary_length(row["label"]), axis=1)
csv.to_csv('tokens.csv', encoding='utf-8')
print('donezo')