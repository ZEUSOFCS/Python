'''
 Author      : DORIAN JAVA BROWN
 Version     : N/A
 Copyright   : All Rights Reserve; You may use, distribute and modify this code.
 Description : This is a simple calculator that can add, subtract, multiply and divide using functions 
 '''




'''function definition'''
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
  


def operation():
  
  operation = raw_input('Enter Operation symbol: ')
  
  # recieving two numbers from user
  num1 = int(raw_input('\nEnter first number  : '))
  num2 = int(raw_input('\nEnter second number : '))
  
  
  '''check if operation symbol is valid'''
  
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
 
  again()

 # ask user if they want to use the calculator again
def again():

    calc_again = raw_input(' \n\n Do you want to calculate again [YES or NO] :  ')

    # If user types Y, run the calculate() function
    if calc_again == 'YES' or calc_again == 'Yes' or calc_again == 'yes':
        calculate()
        operation()
        
    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'NO' or  calc_again == 'No' or calc_again == 'no':
        print('\n\n\t\tApplication Closed.\n\n')

    # If user types another key, run the function again
    else:
        again()

'''function call'''
calculate()
operation()
