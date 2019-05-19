# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:53:21 2019

@author: NITS
"""

from bs4 import BeautifulSoup as bs       #import beautifulsoup library
import pandas as pd                       #import pandas library for dataframe
import requests                           #import requests library
import sqlite3                            #import sqlite library

conn = sqlite3.connect("icc.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS icc_odi")
c.execute("""CREATE TABLE icc_odi(S_NO INTEGER,
                                     COUNTRY_NAME TEXT,
                                     MATCHES INTEGER,
                                     POINTS INTEGER,
                                     RATINGS INTEGER
        )
             """)

source = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text  #call the url 
soup = bs(source,'lxml')                                     #convert the data in html format
#print(soup.prettify())
tab = soup.find('table',class_='table')                     #find the class in the given data
A=[]                           #intialize list
B=[]
for item in tab.findAll('tr'):           #find the 'tr' in the data
    item1 = item.findAll('td')           #find the 'td' in the data
    if len(item1) == 5: 
       A.append(item1[0].text.strip())   #insert the all information in list
       A.append(item1[1].text.strip())  
       A.append(item1[2].text.strip())  
       A.append(item1[3].text.strip())  
       A.append(item1[4].text.strip()) 
       B.append(A)
       A = []

for j in B:
    c.execute("INSERT INTO icc_odi VALUES("+j[0],j[1],j[2],j[3],j[4]+")")
        



