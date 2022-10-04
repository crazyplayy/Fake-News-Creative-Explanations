import pandas as pd
import random
import codecs


csv_p = pd.read_csv('Poems.csv', sep=';')
csv_s = pd.read_csv('Samples.csv', sep=';')
print(csv_p)
n = input('N de exemplos > ')  
nome = 'StanzaStyle-' + str(n) + "InputExamples"

i = 0
selection = [3,4,8,10,11,12,13,14,15,20,21,24,25,26,27,30,31,32,33,34,35,36,40,41,42,43,45,47,48,49,50,53,55,56,58,60,65,66,70,72,73,75,76,78]
lista = []

while i < int(n):
    number = random.choice(selection)

    if number not in lista:
        lista.append(number)
        i += 1

    else:
        i = i

#POEMS   
texto = 'Write me a poem for a given summary taking into account the claim and the label \n' 
for el in lista: 
    id = el - 2    
    rowz = csv_p.loc[int(id)]
    
    c = rowz["claim"]
    l = rowz["label"]
    ss = rowz["summary"]
    p = rowz["poems"]
    
    claim = f'Claim: {c} \n'
    label = f'Label: {l} \n'
    summary = f'Summary Explanation: \n {ss} \n'
    poem = f'Poem: \n {p} \n'
        
    sample = '\n' + claim + label + summary + poem + '\n'
    texto += sample

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

texto = texto.replace('Poem: \n ','Poem: \n').replace('Summary Explanation: \n ','Summary Explanation: \n')

#WRITE
f = codecs.open(nome +'.txt', 'w', 'utf-8')
f.write(texto)
f.close()

print(f'Je suis done')