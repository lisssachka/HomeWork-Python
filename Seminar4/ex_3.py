# Задайте последовательность чисел. Напишите программу, которая выведет список элементов, которые не имели повторов в исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

from random import randint

def Unique_Numbers(list):
    numbers_unique = []
    for i in list:
        if list.count(i) > 1:
            continue
        numbers_unique.append(i)
    return numbers_unique

numbers = [3, 1, 2, 3] # -> 2 1

print(f'Numbers: {numbers}\n')

print(f'Unique numbers: {Unique_Numbers(numbers)}') 