# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Список с клавиатуры
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint

def RandomList(n):
    numbers = []
    for i in range(n):
        numbers.append(randint(-10, 10))
    return numbers

def Composition(list, number):
    comp = 0
    composition_list = []
    for i in range(len(list)):
        while i < len(list)/2 and number > len(list)/2:
            number = number - 1
            comp = list[i] * list[number]
            composition_list.append(comp)
            i += 1
    return composition_list

n = int(input('Enter a numbers of items: '))
list = RandomList(n)
print(list)
print(Composition(list, n))
