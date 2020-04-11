# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:14:51 2020

@author: tiago
"""

#criando scrpit que faz um request de dados para uma API
#organiza os dados usando o Pandas
from urllib.request import urlopen
import pandas as pd
import json

#html = urlopen("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json").read()
#html_json = json.loads(html)
#pandas_html = pd.DataFrame(html_json)
#pandas_html = pandas_html.index(pandas_html['data'])

def get_data_bcb(código):
    url = "http://api.bcb.gov.br/dados/serie/bcdata.sgs."+código+"/dados?formato=json"
    html = urlopen(url).read()
    html_json = json.loads(html)
    pandas_html = pd.DataFrame(html_json)
    return pandas_html

a = get_data_bcb("11")
    
