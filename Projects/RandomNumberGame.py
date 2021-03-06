'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This Guessing Game tries to guess the user number by generating
               a random number between 1 and 5   
 '''

# import the random module
import random

# title of game
print ('\n\n')
print('\tGuessing Game')
print('--------------------------')
print ('')
      
# question for user
print('Think of a number between 0 - 5')
print('')

# declaration of the limit of sayinh no
answerLimit = 0;

# random number between 0 and 5
numGuess = random.randint(0,5)
 
# conditional statements 
while answerLimit >= 0:
  
  answerReady = raw_input('READY ?  [YES/NO] : ')
  
  if answerReady == 'YES' or answerReady == 'yes' or answerReady == 'Yes': 
      print('\n\n')
      print('  ********************')
      print('  *                  *')
      print('  *     I GUESS ' + str(numGuess) + '    *')
      print('  *                  *')
      print('  ********************')
      print('\n')
      
      answerLimit = -1
  elif answerReady == 'NO' or answerReady == 'no' or answerReady == 'No':
  
      print('\nKeep thinking......\n\n')
      print('___________________________________________________\n')
      answerLimit = 1
  else:
      print('\n \n ERROR: invalid input...      Please try again. \n\n')
      answerLimit = 1
      

# declaration of reset to ask the user the question again 
reset = 0

# conditional statements 
while reset >= 0:
  
  # input data from the user
  answerCorrect = raw_input('\nCORRECT ? [YES/NO] : ')
      
  # conditional statements 
  if answerCorrect == 'YES' or answerCorrect == 'yes' or answerCorrect == 'Yes': 
      print('\n\n :' + ')' )
      print('\n\n')
      reset = -1   
  elif answerCorrect == 'NO' or answerCorrect == 'no' or answerCorrect == 'No':
      print('\n\n :' + '(' )
      print('\n\n')
      reset = -1
  else:
     print('\n\nERROR: invalid input...  CODE #0E53')
     print('\nPlease enter \"Yes or No" try again.\n')
     reset = 1
     
      
      
