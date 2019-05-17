# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:35:42 2019

@author: NITS
"""
albha1 = "qwertyuioplkjhgfdsazxcvbnm "
albha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z',' ']
string =['The quick brown fox jumps over the lazy dog']
for i in string:
    for j in i.lower():
       # a = j.split
       for k in albha:
           if k in j:
               n=1
               break
       else:
            print("sentence is not pangram")
            break
if n == 1:
    print('Sentence is pengram')
