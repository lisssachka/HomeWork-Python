# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

from random import randint

def InputNum(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def PrintResult(name, kol, count, value):
    print(f'Игрок {name} взял {kol} конфет. Теперь у него {count}, а на столе {value} конфет')

def Game(value, player1, player2):
    counter1 = 0
    counter2 = 0
    flag = True
    while value > 28:
        if flag:
            k = InputNum(player1)
            counter1 += k
            value -= k
            flag = False
            PrintResult(player1, k, counter1, value)
        else:
            k = randint(1, 29)
            counter2 += k
            value -= k
            flag = True
            PrintResult(player2, k, counter2, value)
            print()
    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")

player1 = "Человек"
player2 = "Бот"
value = 120
Game(value, player1, player2)

