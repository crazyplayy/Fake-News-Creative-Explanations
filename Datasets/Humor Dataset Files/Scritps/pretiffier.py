import pandas as pd
from csv import writer

csv = pd.read_csv('HumorDB_Final.csv', sep=';')

rowz = []

for index, row in csv.iterrows():
    fila = []
    context = row['Context']
    poem = row['Poem']
    humor = row['Humor']
    
    context = context.replace('^^','').replace('\n', '').replace('  ',' ').replace('\xa0','').replace('"','“').replace('““','“')
    
    if poem[0] == '"':
        poem = poem[1:]
    else:
        print('yay')
        
    poem = poem.replace('"',"\n").replace('  ', ' ')
    
    fila.append(context)
    fila.append(poem)
    fila.append(humor)
    rowz.append(fila)
    
with open('DB_Final.csv', 'a+', newline='', encoding='utf-8') as f_object:
    for rowl in rowz:
        writer_object = writer(f_object)
        writer_object.writerow(rowl)
    f_object.close()

print('donezo')