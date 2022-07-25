import pandas as pd
import random
import codecs

csv_p = pd.read_csv('Poems.csv', sep=';')
print(csv_p)

nome = "training-data-poems-dataset"

i = 0
texto = ''

while i < int(csv_p.shape[0]):

    rowz = csv_p.loc[int(i)]
    
    c = rowz["claim"]
    l = rowz["label"]
    ss = rowz["summary"]
    p = rowz["poems"]
    
    claim = f'Claim: {c} \n'
    label = f'Label: {l} \n'
    summary = f'Summary Explanation: \n {ss} \n'
    poem = f'Poem: \n {p} \n'
        
    sample = '\n' + claim + label + summary + poem + '\n' + '<|endoftext|>' + '\n'
    texto += sample

    i += 1

texto = texto.replace('Poem: \n ','Poem: \n').replace('Summary Explanation: \n ','Summary Explanation: \n')

#WRITE
f = codecs.open(nome +'.txt', 'w', 'utf-8')
f.write(texto)
f.close()

print(f'Je suis done')