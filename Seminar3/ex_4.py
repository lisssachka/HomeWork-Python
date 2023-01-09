# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decToBin(n):
    if(n > 1):
        decToBin(n//2)
 
    print(n%2, end=' ')
     
n = int(input('Enter a number: '))
decToBin(n)