# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
#     ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
#     a, b, c, d, e, h - рандом

import random

def create_mn(k):
    list = [random.randint(0, 101) for i in range(k+1)]
    return list

def create_str(sp):
    list = sp[::-1]
    mn = ''
    if len(list) < 1:
        mn = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                mn += f'{list[i]}x^{len(list)-i-1}'
                if list[i+1] != 0:
                    mn += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                mn += f'{list[i]}x'
                if list[i+1] != 0:
                    mn += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                mn += f'{list[i]}'
  
    return mn


k = int(input('Enter a number of natural degree: '))
koef = create_mn(k)
print(create_str(koef))