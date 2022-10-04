import pandas as pd
from csv import writer

csv = pd.read_csv('HumorDB-Quatrain-to-Clean.csv', sep=';')

rowz = []

for index, row in csv.iterrows():
    fila = []

    texto = ''

    c = row["Column1"]
    p = row["Column2"]


    claim = f'Claim: {c} \n'
    poem = f'Poem:'

    samplez = claim + poem + '\n\n###\n\n'
    texto += samplez

    pp = f' {p}'
    poema = ''
    poema = pp + '  END '

    fila.append(texto)
    fila.append(poema)
    rowz.append(fila)

with open('GPT-3 Prepared Data HumorDB-Quatrain.csv', 'a+', newline='', encoding='utf-8') as f_object:
    for rowl in rowz:
        writer_object = writer(f_object)
        writer_object.writerow(rowl)
    f_object.close()

print('donezo')