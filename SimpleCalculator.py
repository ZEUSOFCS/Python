'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This is a simple calculator that can add, subtract, multiply and divide using functions 
 '''



'''function definitions'''

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
  operator(operation)
  
  # recieving two numbers from user
  num1 = int(raw_input('\nEnter first number  : '))
  num2 = int(raw_input('\nEnter second number : '))
  
  # addition
  if operation == '+':
    print('\n\n')
    print('ANSWER:  {} + {} = '.format(num1,num2) + str(num1 + num2))
    print('\n\n')
    
  # subtraction 
  elif operation == '-':
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
    
    
def operator(operation):

      if operation != '+':

        if operation == 3 :
          print('Invalid operator, please run the program again.')
          calculate()

 
  
'''function call'''
calculate()