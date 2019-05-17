# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:29:53 2019

@author: NITS
"""
#n = 6
secret_number = 8
while 1:
    guess_number =int(input("Enter the number="))
    
    if secret_number == guess_number:
         print("Player Win \nComputer lose")
         break
    else:
        if guess_number > secret_number + 2:
            print("Too High value")
        elif guess_number < secret_number-2:
          print("Too Low value")
        print("Computer Win \nPlayer lose")
  # print("Secret number= {}".format(secret_number),"Guess_number= {}. ".format(guess_number)) 
 #  print("Guess left={}".format(n)) 
    n = int(input("if you want to continue the game Press 1 and if not press any key="))
    
    if n==1:
        continue
    else:
        break
    