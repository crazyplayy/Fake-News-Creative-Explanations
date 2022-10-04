from cgitb import html
from bs4 import BeautifulSoup 
import requests
import pandas as pd
from csv import writer

#Buscar a primeira pagina
html_page = requests.get('https://lightpoetrymagazine.com/poems-of-the-week/').text
soup = BeautifulSoup(html_page, 'lxml')

i = 1
examples = []
sep = '”\n—'
end = False

#Até chegar ao limit de 124 paginas
while i <=124:
    print(f'Página atual: {i}')

    #Buscar a coluna principal com os poemas
    main_column = soup.find('div', class_="archive-poems-of-the-week")
    poems = main_column.find_all('article')

    #Para cada poema na coluna
    for poem in poems:

        #Ir buscar contexto e poema
        content = poem.find('div', class_="entry-content")
        pars = content.find_all('p')

        #Eliminar autor
        pars.pop(0)
        contexto = ''
        poema = ''
        k = 0

        "Separar o contexto do poema"
        for par in pars:
            par = par.text + '\n'
            par = par.replace('\U0001f642', '').replace('\u014d', ' o').replace('\u2003', ' ').replace('\u20a4', 'LIBRAS').replace('χέζω', '').replace('βίνέω', '').replace('λαικάζω','').replace('à','a').replace('\u2015','-').replace('\u2033','"').replace('\u0392','BETA').replace('\u2212','-')
            
            if len(pars) == 1:
                continue

            elif len(pars) == 2:
                if k == 0:
                    if par[0] == '“' :
                        if sep in par :
                            end = True
                    par = par.split(sep, 1)[0]
                    contexto += par + '"'
                    k += 1
                elif k == 1:
                    poema += par + ' '

            else:       
                if end == False:
                    if par[0] == '“' :
                        if sep in par :
                            end = True
                    par = par.split(sep, 1)[0]
                    contexto += par + '"'
                else:
                    poema += par + ' \n'

        end = False
        contexto += '\n'
        poema += '\n'

        row = []
        row.append(contexto)
        row.append(poema)

        with open('HumorDB.csv', 'a+', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(row)
            f_object.close()

        
    #Passar à próxima página
    i = i + 1
    next_page = "https://lightpoetrymagazine.com/poems-of-the-week/page/" + str(i)
    html_page = requests.get(next_page).text
    soup = BeautifulSoup(html_page, 'lxml')

print('donezo')



















