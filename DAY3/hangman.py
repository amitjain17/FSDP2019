# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:29:42 2019

@author: NITS
"""

secret_word = ["apple","mango",'grapes']

def game(guess):
            if guess in secret_word:
                print("User wins")
                global n
                n = -1
            else:
                print("computer wins \nwrong answer:",guess)
                n-=1
                
    

n=2
while n>0:
    guess= input("Enter the guess word")
    if guess == 'quit':
            break
    
    game(guess)
    