# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:05:26 2019

@author: NITS
"""

from selenium import webdriver
import matplotlib.pyplot as plt
National_share = []
state_name = []
colors = ['perple', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red' , 'blue']


url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = webdriver.Chrome("E:\Machine learning\DAY8\chromedriver_win32\chromedriver.exe")
source.get(url)

for i in range(1,7):
    new = source.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]').text
    new2 = source.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[2]/a').text
    state_name.append(new2)
    National_share.append(float(new))
max_value = (0.15,0,0,0,0,0)
plt.pie(National_share , explode=max_value , labels=state_name , autopct='%1.2f%%', colors = colors, shadow='True', startangle = 25)
 

