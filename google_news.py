# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:28:46 2019

@author: d805664
"""


import requests
import bs4
import names
import nltk

API_KEY = "7be7045a0a544e10916fcb867df3010d"

query = "Lava Jato"

url = ('https://newsapi.org/v2/everything?'
       'q={}&'
       'apiKey={}'.format(query, API_KEY))
response = requests.get(url)
txt = response.json()["articles"]
text = ""

for i in range(len(txt)):
    url_art = txt[i]["url"]
    html = requests.get(url_art).text
    soup = bs4.BeautifulSoup(html, "lxml")
    ps = soup.find_all("p")
    for p in ps:
        text = text + "\n" + p.get_text()

nomes = names.get_human_names(text)
    
print(nomes)
texto_anal = nltk.Text(text.split())
