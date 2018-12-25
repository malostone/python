import math

number = int(input("Введите число"))
a = 0
for i in str(number):
    i = int(i)
    if i > a:
        a = i
print("Максимальное число", a)

a = int(input("Введите значение переменной а "))
b = int(input("Введите значение переменной b "))

a = a + b
b = a - b
a = a - b
print("Переменная а ", a)
print("Переменная b ", b)


a = int(input("Введите значение переменной а "))
b = int(input("Введите значение переменной b "))
c = int(input("Введите значение переменной c "))

d = (b**2)-4 * a * c

x1 = (-b + math.sqrt(d)) / (2*a) 
x2 = (-b - math.sqrt(d)) / (2*a) 
print("Корень 1", x1)
print("Корень 2", x2)


