import random   

temp = []
def make_card(temp):
    card = []
    while len(card) < 5:
        elem = str(random.randint(1, 90))
        if elem not in temp:
            card.append(elem)
            temp.append(elem)
    card = list(card) + list(' ' * 4)
    random.shuffle(card)
    return card
    
def print_card(temp):
    for _ in range(3):
        print(make_card(temp))

def cross_out(card,keg):
    for line in card:
        for i, el in enumerate(line):
            if el == keg:
                line[i] = '-'
                return True
    return False

def check_card(card):
    for line in card:
        for el in line:
            if type(el) == int:
                return  False
    return True

player_card = make_card(temp)
bot_card = make_card(temp)

kegs = random.sample(range(1, 91), 90)

print("Приветсвтую в игре ЛОТО")
for n, keg in enumerate(kegs):
    print("Текущий бочонок: {}. Осталось бочонков: {}.".format(keg, len(kegs) - n - 1))
    print(" Карточка игрока")
    print_card(player_card)
    print("-------------------")
    print("Карточка компьютера ")
    print_card(bot_card)
    print("-------------------")

    while True:
        answer = input("Зачеркнуть бочонок? Выйти? y/n/q: ")
        if answer == 'q':
            print("Вы вышли из игры.")
            exit()
        elif answer == 'y':
            if not cross_out(player_card, keg):
                print("Текущего боченка в карточке нет, проигрыш.")
                exit()
            break
        elif answer == 'n':
            if cross_out(player_card, keg):
                print("Текущий бочонок в карточке есть, проигрыш.")
                exit()
            break
        else:
            print("Неверная команда")

    cross_out(bot_card, keg)
    if check_card(player_card) and check_card(bot_card):
        print("Ничья.")
    elif check_card(player_card):
        print("Зачеркнуты все цифры, вы победили!")
    elif check_card(bot_card):
        print("Компьютер зачеркнул все цифры, проигрыш!")



    


