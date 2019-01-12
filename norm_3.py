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