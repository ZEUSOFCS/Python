'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This program provides the user with options on how much tip the customer should leave the waiter/waitress
 '''

import os

total = 21.49

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
# menu

print('\n\n\t\t JUICEY BURGER\n\n')
print('')
print('1 Juicey Burger  $ 18.99')
print('1 Orange Drink   $  1.00')
print('-------------------------------------------')
print('')
print('Sub Total:       $ 19.99')
print('Local Tax:       $  1.50')
print('Bill Total:      $ 21.49')
print('\n\n')

answer = raw_input('Correct ?  ')

if answer == 'YES' or answer == 'Yes' or answer == 'yes' :
  cls()
  
  # tip suggestion list
  print('\n\n\t Tip Suggestions')
  print('----------------------------------')
  print('A)  %%20           $ %0.3f' %((total * .20)))
  print('B)  %%15           $ %0.3f' %((total * .15)))
  print('C)  %%10           $ %0.3f' %((total * .10)))
  print('D)   %%5           $ %0.3f' %((total * .05)))
  
  
  
elif answer == 'NO' or answer == 'No' or answer == 'no' :
  print ('\n\n\t\t please wait one moment for assistance...\n\n')
  
else:
      print('\n\n\t\t error:. invaild value \n\n')

#https://www.youtube.com/watch?annotation_id=annotation_3770292585&feature=iv&src_vid=bguKhMnvmb8&v=LtGEp9c6Z-U
