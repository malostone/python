fruits = ["Апельсин", "Банан", "Яблоко", "Дыня", "Арубуз", "Груша"]

print("Вывод: ")

for i, fruits in enumerate(fruits):
    print("#", i + 1, fruits.format(">"))

numbers1 = ["23", "34", "4545", "56", "df", "243"]
numbers2 = ["12", "34", "4545", "sfd6", "df", "sdf12"]
numbers1 = list(set(numbers1) - set(numbers2))
print("Уникальные элементы",numbers1)

numbers3 = [43, 45, 867, 808, 89756, 32]
numbers4 = []

print(numbers3)
for item in numbers3:
    if item%2 == 0:
        numbers4 = numbers4 + [item/4]
    else:
        numbers4 = numbers4 + [item*2]
print(numbers4)