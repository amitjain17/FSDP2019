# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:45:46 2019

@author: NITS
"""

import re                                           #intialize the regular expression
email1 = []                                        #intialize list1
email2 = []                                         #intialize list2
while True:
    email = input("Enter the email_id")          # enter the email id
    if not email:
        break
    email1.append(email)
for item in email1:                                     #check the email is valid or not using regular expression
   if re.findall(r'^[A-Za-z0-9_-]+@[a-z0-9]+.[a-z]{2,4}',item):
       email2.append(item)

email2.sort()                           #sort the email id list
print(email2)
    
        
        
        