
from string import digits
from tempfile import tempdir
from textwrap import fill
from turtle import pos
from types import new_class
from unicodedata import digit
from more_itertools import strip
import pandas as pd
import numpy as np
import requests
import lxml as html
from bs4 import BeautifulSoup as bs #for webscrape
from collections import Counter
import string
#https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
import  json
import re
app_id = "<my_app_id>"
app_key = "<my_app_key>"



print("Hello, this is a program to solve wordle")

print("we are going to start off with the word: CARES")

print("you will be prompted to input the result of the word ")

print("if the letter is GREY, input N in the right position")
print("if the letter is YELLOW, input Y in the right position")
print("if the letter is GREEN, input G in the right position")

print("now lets begin:")


five_w = pd.read_csv(r'/Users/daweimouland/Code/wordle project/five_words.csv')
POSS_ANS = pd.DataFrame()
POSS_ANS['word'] = five_w.iloc[:,1:]
print(POSS_ANS)












###time to build the functions 

#first build the word remover


test = POSS_ANS
def word_rem(letter): #works
  temp = test
  temp = test[test["word"].str.contains(letter) == False]
  return(temp)
 
test = word_rem(letter= "a")


#location confirmer

test = POSS_ANS



def loc_conf(letter, posi):
  c = letter
  new_test = []

  for i in range(len(test)):
    temp = test.iloc[i,0]
    if posi in [pos for pos, char in enumerate(temp) if char == c]:
      new_test.append(test.iloc[i,0])
  fin = pd.DataFrame()
  fin['word'] = new_test
  return(fin)

test = loc_conf("b", 3)

print(test)


#location remover 

test = POSS_ANS

def loc_rem(letter, posi):
  c = letter
  new_test = []

  for i in range(len(test)):
    temp = test.iloc[i,0]
    if posi in [pos for pos, char in enumerate(temp) if char != c]:
      new_test.append(test.iloc[i,0])
  fin = pd.DataFrame()
  fin['word'] = new_test
  return(fin)

test = loc_rem("a", 0)

#must contain 

###NEED TO DO 





############################################

#STATS TIME LEGOOO

############################################

alphabet = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alp = pd.DataFrame()
alp["alp"] = alphabet

print(alp)

#######

#position stats

#######

#### MASTER LIST
POS_1 = POSS_ANS['word'].astype(str).str[0]
POS_1_c = pd.DataFrame()
POS_1_c["count"] = POS_1.value_counts().sort_index().astype(int)
POS_1_c['percent'] = (POS_1_c['count']/ len(POSS_ANS)) *100
print(POS_1_c)



POS_2 = POSS_ANS['word'].astype(str).str[1]
POS_2_c = pd.DataFrame()
POS_2_c["count"] = POS_2.value_counts().sort_index().astype(int)
POS_2_c['percent'] = (POS_2_c['count']/ len(POSS_ANS)) *100
print(POS_2_c)


POS_3 = POSS_ANS['word'].astype(str).str[2]
POS_3_c = pd.DataFrame()
POS_3_c["count"] = POS_3.value_counts().sort_index().astype(int)
POS_3_c['percent'] = (POS_3_c['count']/ len(POSS_ANS)) *100
print(POS_3_c)

POS_4 = POSS_ANS['word'].astype(str).str[3]
POS_4_c = pd.DataFrame()
POS_4_c["count"] = POS_4.value_counts().sort_index().astype(int)
POS_4_c['percent'] = (POS_4_c['count']/ len(POSS_ANS)) *100
print(POS_4_c)


POS_5 = POSS_ANS['word'].astype(str).str[4]
POS_5_c = pd.DataFrame()
POS_5_c["count"] = POS_5.value_counts().sort_index().astype(int)
POS_5_c['percent'] = (POS_5_c['count']/ len(POSS_ANS)) *100
print(POS_5_c)
#############

####for test 
POSt_1 = test['word'].astype(str).str[0]
POSt_1_c = pd.DataFrame()
POSt_1_c["count"] = POSt_1.value_counts().sort_index().astype(int)
POSt_1_c['percent'] = (POSt_1_c['count']/ len(test)) *100
print(POSt_1_c)

POSt_2 = test['word'].astype(str).str[1]
POSt_2_c = pd.DataFrame()
POSt_2_c["count"] = POSt_2.value_counts().sort_index().astype(int)
POSt_2_c['percent'] = (POSt_2_c['count']/ len(test)) *100
print(POSt_2_c)

POSt_3 = test['word'].astype(str).str[2]
POSt_3_c = pd.DataFrame()
POSt_3_c["count"] = POSt_3.value_counts().sort_index().astype(int)
POSt_3_c['percent'] = (POSt_3_c['count']/ len(test)) *100
print(POSt_3_c)

POSt_4 = test['word'].astype(str).str[3]
POSt_4_c = pd.DataFrame()
POSt_4_c["count"] = POSt_4.value_counts().sort_index().astype(int)
POSt_4_c['percent'] = (POSt_4_c['count']/ len(test)) *100
print(POSt_4_c)

POSt_5 = test['word'].astype(str).str[4]
POSt_5_c = pd.DataFrame()
POSt_5_c["count"] = POSt_5.value_counts().sort_index().astype(int)
POSt_5_c['percent'] = (POSt_5_c['count']/ len(test)) *100
print(POSt_5_c)

def guesser(test = test, alp = alp):
  POSt_1 = test['word'].astype(str).str[0]
  POSt_1_c = pd.DataFrame()
  POSt_1_c["count"] = POSt_1.value_counts().sort_index().astype(int)
  POSt_1_c['percent'] = (POSt_1_c['count']/ len(test)) *100
  

  POSt_2 = test['word'].astype(str).str[1]
  POSt_2_c = pd.DataFrame()
  POSt_2_c["count"] = POSt_2.value_counts().sort_index().astype(int)
  POSt_2_c['percent'] = (POSt_2_c['count']/ len(test)) *100
  

  POSt_3 = test['word'].astype(str).str[2]
  POSt_3_c = pd.DataFrame()
  POSt_3_c["count"] = POSt_3.value_counts().sort_index().astype(int)
  POSt_3_c['percent'] = (POSt_3_c['count']/ len(test)) *100
  

  POSt_4 = test['word'].astype(str).str[3]
  POSt_4_c = pd.DataFrame()
  POSt_4_c["count"] = POSt_4.value_counts().sort_index().astype(int)
  POSt_4_c['percent'] = (POSt_4_c['count']/ len(test)) *100
  

  POSt_5 = test['word'].astype(str).str[4]
  POSt_5_c = pd.DataFrame()
  POSt_5_c["count"] = POSt_5.value_counts().sort_index().astype(int)
  POSt_5_c['percent'] = (POSt_5_c['count']/ len(test)) *100

  for i in range(len(test)):
    temp1 = test.iloc[i,:].astype(str).str[0]

    temp2 = test.iloc[i,:].astype(str).str[1]

    temp3 = test.iloc[i,:].astype(str).str[2]

    temp4 = test.iloc[i,:].astype(str).str[3]

    temp5 = test.iloc[i,:].astype(str).str[4]
  


temp1 = test.iloc[0,:].astype(str).str[0]

temp2 = test.iloc[0,:].astype(str).str[1]
temp3 = test.iloc[0,:].astype(str).str[2]
temp4 = test.iloc[0,:].astype(str).str[3]
temp5 = test.iloc[0,:].astype(str).str[4]

