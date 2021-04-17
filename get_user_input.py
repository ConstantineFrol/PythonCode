# =================================Task 1=======================================
while True:
    try:
        number = int(input('Please input a number: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

print('Your number is: ', str(number + 2))

# =================================Task 2=======================================
while True:
    try:
        number = int(input('Please input a number: '))
        if 0 < number < 10:
            break
        else:
            print('Please input a number, between 0 and 10')
    except ValueError:
        print('Wrong input, Please try again.')

print('Your number is: ', str(number ** 2))

# =================================Task 3=======================================

print('================= Medical Card =================\n')
f_name = input('Please input patient name: ')
l_name = input('Please input patient last name: ')
age = int(input('Please input patient age: '))
weight = int(input('Please input patient weight: '))

if age <= 30 and 50 <= weight <= 120:
    print('{}, {}, {} y/o, weight {} - the patient is in good form'.format(f_name,l_name,age,weight))
elif (31 <= age <= 40) and (50 > weight or weight > 120):
    print('%s, %s, %d y/o, weight %d - the patient must look after his wellbeing' %(f_name,l_name,age,weight))
elif age > 40 and 50 > weight or weight > 120:
    print(f_name + ', ' + l_name + ', ' + str(age) + ' y/o, weight ' + str(weight) + ' - the patient needs a doctor attention')
else:
    print('Error: something went wrong!')

