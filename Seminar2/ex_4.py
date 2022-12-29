# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Enter N '))
composition = 1
while n >= 1:
    if n % 2 == 0:
        composition*=n
    n-=1
print(f'Composition = {composition}')

