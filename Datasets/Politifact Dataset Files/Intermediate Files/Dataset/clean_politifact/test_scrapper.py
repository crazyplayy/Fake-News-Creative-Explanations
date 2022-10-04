from cgitb import html
from types import NoneType
from bs4 import BeautifulSoup 
import requests
import pandas as pd

pd.set_option('display.max_colwidth', None)

def find_summary(url):
    
    sumz=''
    
    print(f'Checking url: {url}')
    html_page = requests.get(url).text
    soup = BeautifulSoup(html_page, 'lxml')
    
    center_cols = soup.find('div', class_='short-on-time')
    
    eval = isinstance(center_cols, NoneType)
    
    if eval:
        return sumz
    
    else:
        pars = center_cols.find_all('li')
        
        if pars == []:
            pars = center_cols.find_all('p')
            
        for par in pars:

            clean = ''
            if "\u2022" in par.text:
                clean = par.text.replace('\u2022','')
                final = clean + '\n'

            else:
                #final = par.text.replace('  ', ' ')
                clean = par.text.strip()
                clean = clean.strip('\t')
                final = clean + '\n'
            
            sumz += final
             
        return sumz
            
if __name__ == "__main__":
    #url = input('>')  
    #find_summary(url)
    
    csv = pd.read_csv('war.csv',sep=',')
    csv["summary"] = csv.apply(lambda row: find_summary(row["url"]), axis=1)
    csv.to_csv('final_war.csv', encoding='utf-8')
    print(f'Je suis done')