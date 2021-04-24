import os


# ============================================= Task 1 =============================================
# This is Lesson_10.py
def create_folders(folder_name):
    for folder_id in range(1, 10):
        new_path = os.path.join(os.getcwd(), f'{folder_name}_{folder_id}')
        if os.path.exists(new_path):
            # if a folder with this name exists: skip it
            print(f'folder with name: {folder_name}_{folder_id} exists')
            continue
        else:
            # if no folder with such name: create it
            os.mkdir(new_path)
            print(f'folder with name: {folder_name}_{folder_id} was created')


def delete_folders(folder_name):
    # Get list of all files in this dir
    dir_data = os.listdir()
    result = [i for i in dir_data if folder_name in i]
    if len(result) > 0:
        print(f'Dir with {folder_name} are detected ', end='')
        for dir_name in result:
            os.rmdir(dir_name)
        print(' and removed')
    else:
        print(f'Dir that contains \'{folder_name}\' is not detected')


# ============================================= Task 2 =============================================
# Because this file contains only one function there is no needed to create if __name__ == '__main__':
import modules.rand_num

my_list = [1, 2, 3, 4]
# This is jus another way of doing this
result = getattr(modules.rand_num, 'pick_number')(my_list)
print(result)

# this is my module named 'rand_num.py' inside dir modules
import random as rd


def pick_number(some_list):
    return rd.choice(some_list)


# # ============================================= Task 3 =============================================
# This is main.py
import time
from Lesson_10 import create_folders, delete_folders

create_folders('dir')
time.sleep(2)
delete_folders('dir')
