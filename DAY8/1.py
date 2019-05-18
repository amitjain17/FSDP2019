# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:10:39 2019

@author: NITS
"""

from bs4 import BeautifulSoup
import requests
with open("simple.html") as file:
    a =BeautifulSoup(file,'lxml')
#print(a.prettify())
b = a.find_all('div')
#print(a.div)
print(b[1].text)