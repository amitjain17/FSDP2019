# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:28:05 2019

@author: NITS
"""

import re
list1 = []
list2 = []
while True: 
    mail = input("Enter the E_mail: ")
    if not mail:
        break
    else:
        list1.append(mail)
for item in list1:
    print (item)
    if re.match(r'[a-z0-9_-]+@[a-z0-9]+\.[a-z]{2,4}$',item):
        print("true")
        list2.append(item)
    else:
        print("False")
print(list2)