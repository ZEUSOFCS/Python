'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This program generates a random number between 0 and 5
 '''

# import the random module
import random

# title of game
print('Guessing Game \n\n)

# question
print('Think of a number between 0 - 5')

# input data from the user
userNum  = int(input('Guess a number between 0 - 5 : '))

# random number between 0 and 5
guessNum = print( ' I GUESS ' + random.randint(0,5))

      

answer = input('')
      
# conditional statements 
if (userNum == guessNum):
      
      print('')
      
if (userNum != guessNum):
      
      
      