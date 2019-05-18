# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:52:01 2019

@author: NITS
"""
import requests                    #import library requests

url =" https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=b69148213a221dfaaac2"
cur = requests.get(url)             #call the url using rest API
cur1 = cur.json()                   #convert the file in json format
n = int(input("ENTER the Value of USD: "))
print(cur1["USD_INR"]*n)


