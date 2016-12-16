'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This is a simple calculator that can add, subtract, multiply and divide using functions 
 '''



'''functions definitions'''





def calculate():

  # operation selection from the user
  print('Please type in the math operation you would like to complete:')
  print('-------------------------------------------------------------')
  print('+ for addition')
  print('- for subtraction')
  print('* for multiplication')
  print('/ for division')
  print('\ for modulus')
  print('\n\n')

  operation = input('Enter Operation symbol: ')

  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  if operation == '+' :
    print(' {} + {} = ' + (num1 + num2)').format(num1,num2)
    
  elif operation == '-' :
  
  elif operation == '*' :
    
  elif operation == '/' :
  
  elif operation == '\' :
    
  else :
  
  # addition

  # subtraction

  # multiplication 

  # divison