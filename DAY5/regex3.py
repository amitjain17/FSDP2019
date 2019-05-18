# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:07:13 2019

@author: NITS
"""

import re                             #intialize the regular expression
while 1:
    card_number = input("Enter the card number")         #Enter the card number
    if not card_number:
        break
    elif re.match(r'^[456]{1}([0-9]{15})|(^[456][0-9]{3}[-][0-9]{4}[-][0-9]{4}[-][0-9]{4})', card_number):   #check the card number using regular expression
#        if re.search(r'[0]{4,}|[1]{4,}|[2]{4,}|[3]{4,}|[4]{4,}|[5]{4,}|[6]{4,}|[7]{4,}|[8]{4,}|[9]{4,}',card_number):
#            print("INVALID")                    
#        else:
            print("VALID")
    else:
        print("INVALID")
            
            