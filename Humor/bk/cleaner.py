import pandas as pd
from csv import writer

csv = pd.read_csv('to_clean.csv', sep=';')

rowz = []
sep ='” \n—'
sep1 = '”—'
sep2 = '— T'
sep3 = '\n"'

def clean(context):
    row = []
    part1 = ''
    part2 = ''

    if sep in context:
        part1 = context.split(sep, 1)[0]
        part2 = context.split(sep3, 1)[-1]
    elif sep1 in context:
        part1 = context.split(sep1, 1)[0]
        part2 = context.split(sep3, 1)[-1]
    elif sep2 in context:
        part1 = context.split(sep2, 1)[0]
        part2 = context.split(sep3, 1)[-1]

    row.append(part1)
    row.append(part2)
    rowz.append(row)

            
csv= csv.apply(lambda row: clean(row["Column1"]), axis=1)

with open('cleaned.csv', 'a+', newline='', encoding='utf-8') as f_object:
    for rowl in rowz:
        writer_object = writer(f_object)
        writer_object.writerow(rowl)
    f_object.close()
            

print('donezo')