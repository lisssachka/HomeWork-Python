# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите число: ')

sum_digit = sum(map(int, filter(lambda el: el.isdigit(), num)))

print(sum_digit)