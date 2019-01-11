import random

def my_round(number, ndigits):
    after_point = int(10 ** ndigits)
    shift  = number * after_point
    new_number = int(shift )
    indicator  = int((shift  - new_number) * 10)
    if indicator  >= 5:
        new_number += 1  
    return new_number/after_point

print(my_round(random.uniform(1.0876521, 23.6655665), 5))

def lucky_ticket(ticket_number):
    a = str(ticket_number)
    sum1 = int(a[0]) + int(a[1]) + int(a[2])
    sum2 = int(a[3]) + int(a[4]) + int(a[5])
    if sum1 == sum2:
        return "Счастливый"
    else:
        return "Не счастливый"
        
    
print(lucky_ticket(123006))
print(lucky_ticket(random.uniform(111111, 999999)))
