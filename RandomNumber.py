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
print('\tGuessing Game')
print('--------------------------')
print ('')
      
# question for user
print('Think of a number between 0 - 5')
print('')

# declaration of the limit of sayinh no
#answerLimit = 0;

# random number between 0 and 5
numGuess = random.randint(0,5)
 
#while answerLimit < 3:
  
answerReady = raw_input('READY ? (YES/NO) : ')

if answerReady == 'Yes' or answerReady == 'yes' : 
     
      print('')
      print('I GUESS ' + str(numGuess))
      print('')
elif answerReady == 'NO' or answerReady == 'no' :
      
      print('\nKeep thinking......\n\n')
else:
      print('\ninvalid input')
      print('\n Please try again...')
      
# input data from the user
answerCorrect = raw_input('CORRECT? (YES/NO) : ')
      
# conditional statements 

if answerCorrect == 'YES' or answerCorrect == 'yes' :
     
      print('\n OU OHHH YEAHHH!')
      print('\n\n')
elif answerCorrect == "NO" or answerCorrect == "no" :
      
      print("\nNope :" + "( " + "Try again !")
      print('\n\n')
else:
  
      print("invalid input")
      
      