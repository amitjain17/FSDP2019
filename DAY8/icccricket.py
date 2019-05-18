# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:30:01 2019

@author: NITS
"""
from bs4 import BeautifulSoup as bs       #import beautifulsoup library
import pandas as pd                       #import pandas library for dataframe
import requests                           #import requests library

source = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi').text  #call the url 
soup = bs(source,'lxml')                                     #convert the data in html format
#print(soup.prettify())
tab = soup.find('table',class_='table')                     #find the class in the given data
A=[]                           #intialize list
B=[]
C=[]
D=[]
E=[]
for item in tab.findAll('tr'):           #find the 'tr' in the data
    item1 = item.findAll('td')           #find the 'td' in the data
    if len(item1) == 5: 
       A.append(item1[0].text.strip())   #insert the all information in list
       B.append(item1[1].text.strip())  
       C.append(item1[2].text.strip())  
       D.append(item1[3].text.strip())  
       E.append(item1[4].text.strip()) 
#str2 = OrderedDict([A,B,C,D,E])
str2 = [A,B,C,D,E]                      #create string of given data
value = pd.DataFrame(str2)               #create a table of given information
       
       

