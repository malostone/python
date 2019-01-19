#scripts

import os

def change_dir_path(dirname):
    if not dirname:
        print("Нужно указать имя директории")
        return
    try:
        os.chdir(dirname)
        return print("Вы перешли в директорию ", dirname)
    except FileNotFoundError:
        return print("Невозможно перейти в эту директорию")

def create_dir(new_dir):
    if not new_dir:
        print("Нужно указать имя новой папки")
        return
    try:
        os.mkdir(new_dir)
        return print("Папка", new_dir,  "была успешно создана")
    except FileExistsError:
        return print("Папка", new_dir, "уже создана")

def delete_dir(del_dir):
    if not del_dir:
        print("Нужно указать имя папки которую хотите удалить")
        return
    try:
        os.rmdir(del_dir)
        return print("Вы удалили папку ", del_dir)
    except FileExistsError:
        return print("Невозможно удалить ", del_dir)
    except FileNotFoundError:
        return print("Такой папки не существует ", del_dir)

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