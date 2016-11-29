'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This program generates a random number between 0 and 5
 '''

# import the random module
import random

# title of game
print ('')
print('Guessing Game')
print('------------------------')
print ('')
      
# question for user
print('Think of a number between 0 - 5')
print('')

# random number between 0 and 5
numGuess = random.randint(0,5)

# procrastination to by time from user 
print('Keep thinking......\n\n')
answerReady = raw_input('READY ? (YES/NO) : ')

if answerReady == 'Yes' or 'yes' :
      
      print('')
      print('I GUESS ' + str(numGuess))
      print('')
else: 
      print('Keep thinking......\n\n')
      answerReady = input('READY? (YES/NO) : ')
      
# input data from the user
answerCorrect = raw_input('CORRECT? (YES/NO) : ')
      
# conditional statements 
if answerCorrect == 'YES' or 'yes' :
      
      print('\nOHHH YEAHHH! I AM A SAVAGE')
      
if answerCorrect == 'NO' or 'no':
      
      print('\nAWE No :' + '( ' + 'Try again !')
      
      
      