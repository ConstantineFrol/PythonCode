# ========================================== Task 1 ==========================================
import random
import time


def user_data(name, age, town):
    return f'{name}, {age} y/o, lives in {town}'


print(f'Employee of the year: {user_data("John", 35, "London")}')

# ========================================== Task 2 ==========================================
numbers = []


def get_three_numbers():
    global numbers
    while len(numbers) < 3:
        try:
            number = int(input('Please input a number: '))
            numbers.append(number)
        except ValueError:
            print('Wrong input, Please try again.')
    return numbers


# Version 1
print(f'The biggest number is: {max(get_three_numbers())}')
# Version 2
print(max(numbers, key=lambda x: x))

# ========================================== Task 3 ==========================================
# Global var
enemy = ''
hero = ''
armor = 1.2


# display whose won
def check_health():
    if enemy['health'] > hero['health']:
        print(f'The winner is: {enemy["name"]}')
    else:
        print(f'The winner is: {hero["name"]}')


# Fight process
def attack_process(player):
    if player == 'hero':
        print(f'{hero["name"]} is attacking {enemy["name"]}')
        enemy["health"] -= calculate_damage(hero["damage"])
        print(f'{enemy["name"]} health is: {enemy["health"]}\n')
    else:
        print(f'{enemy["name"]} is attacking {hero["name"]}')
        hero["health"] -= calculate_damage(enemy["damage"])
        print(f'{hero["name"]} health is:  {hero["health"]}\n')


# Get input from user
def get_input(role):
    while True:
        name = input(f'\ninput {role} name: ')
        if name.isalpha():
            return create_character(role, name)


# Create dict
def create_character(role, name):
    character = {
        'name': name,
        'health': random.randint(50, 100),
        'damage': random.randint(10, 50)
    }
    print(f'{role.upper()}:')
    for key, val in character.items():
        print(f'{key} : {val}')
    return character


# ask user give names
def get_names():
    global enemy
    global hero
    enemy = get_input('enemy')
    hero = get_input('hero')


# generate whose turn to attack
def random_move():
    whose_turn = random.randint(1, 100)
    if whose_turn <= 50:
        attack_process('enemy')
    else:
        attack_process('hero')


def start_game():
    get_names()
    print('\nthe game starts in')
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('!!! Fight !!!\n')
    while enemy['health'] >= 0 and hero['health'] >= 0:
        random_move()
        time.sleep(1)
    check_health()


# ========================================== Task 4 ==========================================
def calculate_damage(damage):
    return int(damage / armor)


start_game()
