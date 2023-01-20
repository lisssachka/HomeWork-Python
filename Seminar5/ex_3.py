# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

import os.path
from pathlib import Path

def CompressRle(str):
    count = 1
    res = ''

    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            count += 1

        else:
            res += f'{count}{str[i]}'
            count = 1

    if count > 1 or str[-2] != str[-1]:
        res += f'{count}{str[i]}'

    return res


def DecompressRle(str):
    number = ''
    res = ''
    for i in range(len(str)):
        if str[i].isdigit():
            number += str[i]
        else:
            res += str[i] * int(number)
            number = ''
    return res


BASE_DIR = Path(__file__).resolve().parent

with open(os.path.join(BASE_DIR, 'file.txt'), 'r') as f:
    data = f.read()

comp = CompressRle(data)
print(comp)
print(DecompressRle(comp))
