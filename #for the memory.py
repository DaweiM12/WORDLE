#for the memory 
#basically if the word was used in the last 30 days remove it from a list of possible answers

from more_itertools import strip
import pandas as pd
import numpy as np
import requests
import lxml as html
from bs4 import BeautifulSoup as bs #for webscrape
from collections import Counter
#https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
import  json
import re





url = "https://bmcri.org/wordle/"

link = requests.get(url)
soup = bs(link.text, "html.parser")

t = soup.find_all('figure', class_= 'wp-block-table')[1].find('table').find('tbody').find_all('tr')

Word_list = []

for row in t:
    Word = row.find_all('td')[2].text #good
    Word_list.append(Word)

Prev_ANS = pd.DataFrame()
Prev_ANS['Word'] = Word_list

Prev_ANS = Prev_ANS.iloc[2:,:]