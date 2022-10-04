import pandas as pd
from csv import writer

csv = pd.read_csv('PoemsDB.csv', sep=';')

rowz = []

for index, row in csv.iterrows():
    fila = []

    texto = ''

    c = row["claim"]
    l = row["label"]
    ss = row["summary"]
    p = row["poems"]

    claim = f'Claim: {c} \n'
    label = f'Label: {l} \n'
    summary = f'Summary Explanation: \n {ss} \n'
    poem = f'Poem:'

    samplez = claim + label + summary + poem + '\n\n###\n\n'
    texto += samplez

    texto = texto.replace('Summary Explanation: \n ','Summary Explanation: \n')

    pp = f' {p}'
    poema = ''
    poema = pp + '  END '

    fila.append(texto)
    fila.append(poema)
    rowz.append(fila)

with open('GPT-3 Prepared Data PoemsDB.csv', 'a+', newline='', encoding='utf-8') as f_object:
    for rowl in rowz:
        writer_object = writer(f_object)
        writer_object.writerow(rowl)
    f_object.close()

print('donezo')