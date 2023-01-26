from os.path import exists, join
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_data(file_path = 'phone_book.csv'):
    if exists(join(BASE_DIR, file_path)):
        with open(join(BASE_DIR, file_path), 'r', encoding='utf-8') as f:
            book_data = f.readlines()

        for i in range(len(book_data)):
            book_data[i] = book_data[i].strip('\n')
            book_data[i] = book_data[i].split(', ')
        return book_data
    return 'В телефонной книге нет записей!'

def export_data(data, file_path = 'phone_book.csv'):
    with open(join(BASE_DIR, file_path), 'a', encoding='utf-8') as f:
        f.write(data)

def format_data(data, file_type = 'csv', delimiter = '*'):
    data_fields = ['Фамилия: ', 'Имя: ', 'Номер телефона: ', 'Описание: ']

    if file_type == 'csv':
        format_data = ', '.join(data) + '\n'
    elif file_type == 'txt':
        format_data = data[:]
        for i in range(len(format_data)):
            format_data[i] = data_fields[i] + format_data[i]
        format_data.append(delimiter * 15 + '\n')
        format_data = '\n'.join(format_data)

    else:
        format_data = 'None\n'

    return format_data