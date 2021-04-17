import random
import time

# ========================== The best game in the universe ==========================
# Variables
secret_number = None
computer_number = -1
min_value = 1
max_value = 100
validation = False

# Print rules:
print('Rules: \nYou need to think of secret-number from 1 to 100 and your computer will try to guess this number\n'
      'if your secret-number will be higher than computers you must type in: <\n'
      'if your secret-number will be lower than yours computer number then type in: >\n'
      'and if some how your computer will guess your secret-number type in: = \n')

# Get validated input from user
while True:
    try:
        secret_number = int(input(f'Please input a secret number from {min_value} to {max_value}: '))
        if 1 <= secret_number <= 100:
            break
        else:
            print('Error, your number must be between 1 and 100')
    except ValueError:
        print('Wrong input, Please try again.')

# Start the game
print('the game starts in')
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print('Go')
user_validation = ''

# The Game
numbers = []
try_count = 0
computer_number = random.randint(min_value, max_value)
while True:
    try_count += 1
    print(f'I hope your secret number is : {computer_number}', end='')

    user_validation = input(' ')
    if user_validation == '>' or user_validation == '<' or user_validation == '=':
        print(user_validation)
        if user_validation == '>':
            max_value = computer_number - 1

        elif user_validation == '<':
            min_value = computer_number + 1

        else:
            print(f'Computer won, after {try_count} tries')
            break

    else:
        print('Wrong input, Please try again.')

    computer_number = random.randint(min_value, max_value)
    for number in numbers:
        if number == computer_number:
            computer_number = random.randint(min_value, max_value)

    numbers.append(computer_number)
