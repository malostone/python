# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n, m):
    i = 2
    fib_numbers =[1,1]
    while i < m:
        a = fib_numbers[i-1] + fib_numbers[i-2]
        fib_numbers.append(a)
        i = i + 1
    
    return fib_numbers[n - 1: m]

n = input("Начальное значение элемента ряда Фибоначчи ")
n = int(n)
m = input("Конечное значение элемента ряда Фибоначчи ")
m = int(m)
print(fib(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(list):
    n = 1 
    while n < len(list):
        for i in range(len(list)-n):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1],list[i]
        n += 1
    
    return list

print(sort_to_max([-1, 0 , 2, 57, 45, 19, 9, -7, 32, 43]))
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def find_x(string):  
    return 'x' in string.lower()

list = ['extreme', 'vector', 'x-ray', 'helicopter', 'x-mas']

def my_filter(find_x, list):
    for i in list:
        if find_x(i) == False:
            list.remove(i)
    return list

print(my_filter(find_x, list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def side_parl(a: tuple,b: tuple):
    x1,y1 = a
    x2,y2 = b
    side = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return side


def it_parallelogram(point1: tuple, point2: tuple, point3: tuple, point4: tuple):
    if side_parl(point1,point2) == side_parl(point3,point4) and side_parl(point2,point3) == side_parl(point4,point1):
        return "Это параллелограмм"
    else:
        return "Не параллелограмм"
    

print(it_parallelogram((1,3), (4,7), (2,8), (-1,4)))

