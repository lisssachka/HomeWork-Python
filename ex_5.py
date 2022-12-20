# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = int(input('Enter a x for first point '))
ay = int(input('Enter a y for first point '))
bx = int(input('Enter a x for second point '))
by = int(input('Enter a y for second point '))

import math
distance = math.sqrt((bx-ax)**2+(by-ay)**2)
print(f'Distance from A to B = {distance}' )