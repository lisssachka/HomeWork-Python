# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input('Enter N '))
mindivider = 2
while n % mindivider !=0:
    mindivider+=1
print(f'Min divider = {mindivider}')