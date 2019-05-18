11# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:09:03 2019

@author: NITS
"""

from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
import requests
import time

url ="https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("E:\Machine learning\DAY8\chromedriver_win32\chromedriver.exe")
u = browser.get(url)

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
for i in range(1,11):
       url = '''//*[@id="pagi_content"]/div[1]/div['''+ str(i) +''']/p[1]/a'''
       bid_name =  browser.find_element_by_xpath(url)
       a.append(bid_name.text)
       