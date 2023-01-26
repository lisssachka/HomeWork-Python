from model import format_data, get_data, export_data
from view import console_view

def export_data_to_book(data):
    data_csv = format_data(data)
    data_txt = format_data(data, 'txt')
    export_data(data_csv)
    export_data(data_txt, 'phone_book.txt')

def validate_user(user_choice, valid_choices, msg = 'Ваш выбор: '):
    while user_choice not in valid_choices:
        print('Введите правильный вариант!')
        user_choice = input(msg)
    return user_choice


def user_interface():
    main_menu = [
        'Доступные действия',
        '1. Добавить новый контакт',
        '2. Показать список контактов',
        'Ваш выбор: '
        ]
    export_fields = [
        'фамилия',
        'имя',
        'номер телефона',
        'описание',
    ]

    console_view(main_menu, end='')
    user_choice = input()
    user_choice = validate_user(user_choice, ['1', '2'])

    if user_choice == '1':
        new_data = []

        for i in range(len(export_fields)):
            field = input(f'Введите {export_fields[i]}: ')
            new_data.append(field)

        export_data_to_book(new_data)

    elif user_choice == '2':
        book = get_data()
        fields = export_fields[:]
        fields[0] = 'фамилия'
        if type(book) == list:
            delimiter = '*' * 20
            print(delimiter)

            book = [[f'{fields[i].capitalize()}: {el[i]}'
                              for i in range(len(el))]
                            for el in book]

            book = ['\n'.join(el) for el in book]

            for i in range(1, len(book) * 2 , 2): 
                book.insert(i, delimiter)

        console_view(book)

if __name__ == '__main__':
    user_interface()