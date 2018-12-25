import random

number = random.randrange(1, 20)

while number >0:
    print("Цифры исходного кода ", number)
    number = number - 1

    
a = int(input("Введите значение переменной а "))
b = int(input("Введите значение переменной b "))

c = a-b
a = a-c
b=b+c
print(a)
print(b)

age = int(input("Введите свой возраст "))
if age >=18:
    print("Доступ разрешен")
else:
    print("В доступе отказано")

