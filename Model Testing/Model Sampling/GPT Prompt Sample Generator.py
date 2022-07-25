import pandas as pd
import random
import codecs

csv_p = pd.read_csv('Poems.csv', sep=';')
csv_s = pd.read_csv('Samples.csv', sep=';')

n = input('N de exemplos > ')  
nome = 'InputSampleWith' + str(n) + "ExampleClaims"

i = 0
lista = []

while i < int(n):
    number = random.randint(0,74)

    if number not in lista:
        poema = csv_p.loc[int(number)]["poems"]
        eval = isinstance(poema, float)
        lista.append(number)
        i += 1

    else:
        i = i

#POEMS   
texto = 'Write me a poem for a given summary taking into account the claim and the label \n' 
for el in lista:      
    rowz = csv_p.loc[int(el)]
    
    c = rowz["claim"]
    l = rowz["label"]
    ss = rowz["summary"]
    p = rowz["poems"]
    
    claim = f'Claim: {c} \n'
    label = f'Label: {l} \n'
    summary = f'Summary Explanation: \n {ss} \n'
    
    eval2 = isinstance(p, float)
    if eval2:
        p = ''
            
    poem = f'Poem: \n {p} \n'
        
    sample = '\n' + claim + label + summary + poem + '\n'
    texto += sample

#texto = texto.replace('\n', ' ')

#SAMPLE
id = random.randint(0,948)
rowz = csv_s.loc[id]
    
c = rowz["claim"]
l = rowz["label"]
ss = rowz["summary"]
p = rowz["poems"]

claim = f'Claim: {c} \n'
label = f'Label: {l} \n'
summary = f'Summary Explanation: \n {ss} \n'
poem = f'Poem: \n'

samplez = '\n' + claim + label + summary + poem + '\n'
texto += samplez

#WRITE
f = codecs.open(nome +'.txt', 'w', 'utf-8')
f.write(texto)
f.close()

print(f'Je suis done')