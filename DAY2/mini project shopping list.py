# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:50:36 2019

@author: NITS
"""

shopping_list = []
list1= []
print("What do you from store")
x = 1
def help():
        print("Enter DONE when you complete your shopping")
        print("Enter SHOW when you want to see what is in your list")
        print("Enter HELP when you want to see the help")

while 1:
    
    new_item = str(input("Enter the product you want"))
    if new_item == "REMOVE" or new_item == 'Remove' or new_item == 'remove':
        shopping_list.remove(new_item)
        continue
    if (new_item == 'HELP' or new_item == 'Help' or new_item == 'help'):
        help()
        continue
    if new_item == 'SHOW' or new_item == 'Show' or new_item == 'show':
        print(shopping_list)
        continue
   
    if new_item == 'DONE' or new_item == 'Done' or new_item == "done":
       break
    shopping_list.append(new_item)
for i in shopping_list:
    print(x,end=" ")
    print(i)
    x+=1
    