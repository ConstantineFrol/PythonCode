# ======================================== Task 1 ========================================
my_list_1 = [2, 5, 8, 2, 12, 12, 3, 3, 3, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
my_list_2 = [2, 7, 12, 3]

remove_duplicates = lambda list_1, list_2: list(filter(lambda element: element not in my_list_2, my_list_1))
my_list_1 = remove_duplicates(my_list_1, my_list_2)

print(my_list_1)

# OR

result = set(my_list_1) - set(my_list_2)
print('The shortest way: {}'.format(result))

# # ======================================== Task 2 ========================================
my_date = '02.11.2013'

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

dates = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
         'eleventh''twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth',
         'nineteenth', 'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth',
         'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 'twenty-ninth', 'thirtieth', 'thirty-first']

converted_list = list(map(int, my_date.split('.')))
print('Your date is: The {} of {}, {}'.format(dates[converted_list[0] - 1], months[converted_list[1] - 1],
                                              converted_list[2]))

# # ======================================== Task 3 ========================================
my_list_3 = list(dict.fromkeys(my_list_1))

print('Remove all duplicates: {}'.format(my_list_3))
