# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:59:44 2019

@author: NITS
"""
import matplotlib.pyplot as mp
from selenium import webdriver
list1=[]
list2=[]
url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = webdriver.Chrome("E:\Machine learning\DAY8\chromedriver_win32\chromedriver.exe")
source.get(url)
for i in range(1,7):
    a = source.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]').text
    list2.append(float(a))
    b= source.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[2]/a').text
    list1.append(b)
explode=(0.1,0,0,0,0,0)
mp.pie(list2,explode=explode, labels=list1 ,autopct="%1.2f%%")
