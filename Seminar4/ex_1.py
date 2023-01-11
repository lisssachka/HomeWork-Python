# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())
def Pi(n):
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-n-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return (pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2

import math
def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

n = int(input('Enter the number of decimal places): '))
print(f'With an accuracy {n}, of pi = {truncate(Pi(n), n)}')