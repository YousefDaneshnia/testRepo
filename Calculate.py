import os
import math
from pyfiglet import figlet_format
from termcolor2 import colored

os.system('clear')

print(colored('===========================================', color='blue'))
print(colored(figlet_format('Welcome'), color='cyan'))
print(colored('===========================================', color='blue'))

print('                                           ')

print(colored('===========================================', color='yellow'))
print(colored('Start Working With Calculator:', color='yellow'))
print(colored('===========================================', color='yellow'))

print('                                           ')

print(colored('===========================================', color='red'))

while True:
    user_op = input('''
    You can choose on of these operations:
    [+] 
    [-]
    [*]
    [/]
    [**]
    [!]
    [root]
    [out]
    Enter your operation: ''')

    if user_op == '+':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print(f'{num1} + {num2} ===> {num1 + num2}')
    elif user_op == '-':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print(f'{num1} - {num2} ===> {num1 - num2}')
    elif user_op == '*':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print(f'{num1} * {num2} ===> {num1 * num2}')
    elif user_op == '/':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        if num2 == 0:
            print(colored('Division by zero is impossible!', color=red))
        else:
            print(f'{num1} / {num2} ===> {num1 / num2}')
    elif user_op == '**':
        num1 = float(input('Enter number 1: '))
        num2 = float(input('Enter number 2: '))
        print(f'{num1} ** {num2} ===> {num1 ** num2}')
    elif user_op == '!':
        num = int(input('Enter number: '))
        print(f'{num}! ===> {math.factorial(num)}')
    elif user_op == 'root':
        num = int(input('Enter number: '))
        print(f'second root({num}) ===> {math.sqrt(num)}')
    elif user_op == 'out':
        print(colored('===================================================', color='blue'))
        print(colored(figlet_format('Good Luck'), color='cyan'))
        print(colored('===================================================', color='blue'))
        break
    else:
        print(colored('Choose again just between defined operations: ', 'yellow'))



