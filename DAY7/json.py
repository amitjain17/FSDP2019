# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:56:31 2019

@author: NITS
"""


import requests                         #import the library requests
url1 ="http://api.openweathermap.org/data/2.5/weather"        
url2 ="?q=jaipur"
url3 ="&APPID=9a203b494a13fc323c3796f7cb0a0666"

url = url1 + url2 + url3                #combine the url
weather = requests.get(url)          #call the url 
weath = weather.json()                 #convert the data in json format

print("coordinates = ",weath['coord'])
print("Weather=",weath['weather'][0]['main'])
print("Wind=",weath['wind']['speed'])
print("Sunset and Sunrise=",weath['sys']['sunrise'],"and",weath['sys']['sunset'])

