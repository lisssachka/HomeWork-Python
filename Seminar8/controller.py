from os.path import exists, join
from pathlib import Path

from model import (BASE_DIR, DISCIPLINES_DIR, get_disciplines_dict, get_pupil_dict, write_data)
from search import search_discipline, search_pupil


def add_pupil(discipline, pupil_name, grade):
    write_data(join(DISCIPLINES_DIR, f'{discipline}.txt'),
               f'{pupil_name} {grade}',
               'a')


def add_grade(discipline, student_name, grade):
    stud_dict = get_pupil_dict(discipline)

    stud_dict[student_name].append(grade)

    write_data(join(DISCIPLINES_DIR, f'{discipline}.txt'), stud_dict)


def user_interface():
    print('Выберите роль:\n1. Преподаватель\n2. Ученик\n')

    decision = input('Ваша роль: ')

    if decision == '1':
        print('\nСписок предметов:')
        print('\n'.join(get_disciplines_dict().keys()) + '\n')

        discipline = input('Введите название предмета: ')

        search_res = search_discipline(discipline)

        if search_res[0]:
            pupil = input('Введите фамилию ученика: ').capitalize()

            if not search_pupil(search_res[1], pupil):
                grade = input('Введите оценку: ')

                add_pupil(search_res[1], pupil, grade)

            else:
                grade = input('Введите оценку: ')

                add_grade(search_res[1], pupil, grade)

        else:
            print('Введите предмет из списка!')

    elif decision == '2':
        surname = input('Введите вашу фамилию: ')

        for name, filename in get_disciplines_dict().items():
            if search_pupil(filename, surname):
                print(f'{name}: {", ".join(get_pupil_dict(filename)[surname])}')


if __name__ == "__main__":
    user_interface()