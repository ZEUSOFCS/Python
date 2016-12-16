'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This is a simple calculator that can add, subtract, multiply and divide using functions 
 '''



'''functions definitions'''




def calculate():

  # operation selection from the user
  print('\n\n')
  print('\t\t\tOperation Selection')
  print('-------------------------------------------------------------')
  print('+ for addition')
  print('- for subtraction')
  print('* for multiplication')
  print('/ for division')
  print('\ for modulus')
  print('\n\n')

  operation = raw_input('Enter Operation symbol: ')

  num1 = int(raw_input('\nEnter first number  : '))
  num2 = int(raw_input('\nEnter second number : '))

  if operation == '+':
    print("\n\n")
    print('ANSWER:  {} + {} = '.format(num1,num2) + str(num1 + num2))
    print("\n\n")
    
    
  elif operation == '-':
    print("\n\n")
    print('ANSWER:  {} - {} = '.format(num1,num2) + str(num1 - num2))
    print("\n\n")
  
  elif operation == '*':
    print("\n\n")
    print('ANSWER:  {} * {} = '.format(num1,num2) + str(num1 * num2))
    print("\n\n")
    
  elif operation == '/':
    print("\n\n")
    print('ANSWER:  {} / {} = '.format(num1,num2) + str(num1 / num2))
    print("\n\n")
  
  elif operation == '\':
    print("\n\n")
    print('ANSWER:  {} \ {} = '.format(num1,num2) + str(num1 % num2))
    print("\n\n")
  
    
  else:
    print('You have not typed a valid operator, please run the program again.')
    
    
    
  
  # addition

  # subtraction

  # multiplication 

  # divison
  
  '''
  
  
  
calculate()