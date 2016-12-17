'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This is a simple calculator that can add, subtract, multiply and divide using functions 
 '''




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

  # check if operation symbol is valid



  # addition
  if operation == '+':
    userData(num1, num2)
    print('\n\n')
    print('ANSWER:  {} + {} = '.format(num1, num2) + str(num1 + num2))
    print('\n\n')
    
  # subtraction 
  elif operation == '-':
    userData()
    print('\n\n')
    print('ANSWER:  {} - {} = '.format(num1,num2) + str(num1 - num2))
    print('\n\n')
    
  # multiplication 
  elif operation == '*':
    print('\n\n')
    print('ANSWER:  {} * {} = '.format(num1,num2) + str(num1 * num2))
    print('\n\n')
    
  # divison
  elif operation == '/':
    print('\n\n')
    print('ANSWER:  {} / {} = '.format(num1,num2) + str(num1 / num2))
    print('\n\n')
  
  # modulus 
  elif operation == '/':
    print('\n\n')
    print('ANSWER:  {} \ {} = '.format(num1,num2) + str(num1 % num2))
    print('\n\n')
  
    
  else: print('Invalid character, please run the program again.')
    
    
def userData(num1, num2):
  # recieving two numbers from user
  num1 = int(raw_input('\nEnter first number  : '))
  num2 = int(raw_input('\nEnter second number : '))
  return num1, num2

 
'''function definitions'''
num1 = userData(num1, num2)
num2 = userData(num1, num2)

  
'''function call'''
calculate()