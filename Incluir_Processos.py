
# coding: utf-8

# In[ ]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def processo(url):

    get = urlopen(url) 
    bsObj = BeautifulSoup(get, 'html.parser'):
    
    for dados in bsObj.find_all('table', attrs={'class':'secaoFormBody'}): 
        processo = dados.select('span')[0].text.strip() 
        classe   = dados.select('span')[3].text.strip() 
        juiz     = dados.select('span')[12].text.strip() 
        valor    = dados.select('span')[-1].text.strip()
    
    for dados in bsObj.find_all('table', attrs={'id':'tableTodasPartes'}): 
        partes = dados.select('span')[0].text.strip() 
        partes += dados.find('td').find_next_sibling('td').text.strip()
        partes += ' ' + dados.select('span')[2].text.strip() 
        partes += dados.select('td')[3].text.strip() 
        partes += ' ' + dados.select('span')[2].text.strip() 
        partes += dados.select('td')[5].text.strip()
    
    for dados in bsObj.find_all('tbody', attrs={'id':'tabelaUltimasMovimentacoes'}): 
        ultima_mov  = dados.select('td')[0].text.strip() 
        ultima_mov += ' ' + dados.select('td')[2].text.strip()
    
    data = []
    data.append({'numero_processo':processo,
             'valor_causa':valor,
             'classe':classe,
             'juiz':juiz,
             'partes':partes,
             'ultima_movimentacao':ultima_mov
            })
    
    return json.dumps(data)

