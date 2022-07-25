import pandas as pd
import random
import codecs

csv = pd.read_csv('DB.csv', sep=';')

print(csv)

nome = input('Nome > ')  
n = input('Quantas samples? ')
i = 0

lista = []
while i < int(n):
    number = random.randint(0,100)
    if number not in lista:
        poema = csv.loc[int(n)]["poems"]
        eval = isinstance(poema, float)
        if eval:
            lista.append(number)
            i += 1
        else:
           i = i
    else:
        i = i

print(f'lista : {lista}')

texto = '' 
for el in lista:      
    rowz = csv.loc[int(el)]
    
    d = rowz["date"]
    c = rowz["statement"]
    l = rowz["truth_o_meter"]
    s = rowz["url"]
    ss = rowz["summary"]
    
    date = f'Date: {d} \n'
    claim = f'Claim: {c} \n'
    label = f'Label: {l} \n'
    source = f'Source: {s} \n \n'
    summary = f'Summary Explanation: \n {ss} \n'
    poem = f'Poem: \n'
    
    sample = '\n' + date + claim + label + source + summary + poem + '\n --------------------- \n'
    texto += sample

f = codecs.open(nome +'.txt', 'w', 'utf-8')
f.write(texto)
f.close()

print(f'Je suis done')

    