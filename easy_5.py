import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

dir_path = os.path.join(os.getcwd(), "dir_")

def create_dir():
    for i in range(1,10):
        try:
            os.mkdir(dir_path + str(i))
        except FileExistsError:
            return("Директории уже существуют")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    dir_list = os.listdir()
    list1 = []
    list2 = []
    for i in dir_list:
        if i.endswith('.py'):
            list2.append(i)
        else:
            list1.append(i)
    return list1
            

    
def delete_dir():
    i = 0
    dir_list = os.listdir()
    while i < len(dir_list):
        os.rmdir(dir_list[i])
        i += 1

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
        
def copy_current_file():
    current_file = os.path.realpath(__file__)
    copy_file = current_file.replace('.py', '_copy.py')
    shutil.copy(current_file, copy_file)


print(create_dir())
print(list_dir())
print(copy_current_file())      
        
