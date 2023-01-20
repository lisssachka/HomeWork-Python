# Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
def PrintField(field):

    for el in field:
        el_str = ' ' + ' | '.join(map(str, el)) + ' '

        if el == field[-1]:
            print(el_str)

        else:
            print(el_str)
            print('___________')


def CheckCell(pos, field, is_player: bool = True):

    in_row = 3

    if 0 < pos < 10:
        pos_x = [2, 0, 1][pos % in_row]
        pos_y = int(pos > in_row) + int(pos > in_row * 2)

        if field[pos_y][pos_x] == pos:
            return True

    if is_player:
        print('Клетка занята или находится вне диапазона [1-9]')

    return False


def CheckWin(field, character):
    win = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    )

    for positions in win:
        values = [field[position[0]][position[1]] for position in positions]
        if all(el == character for el in values):
                return True

    return False


def RestartGame():
    decision = input('Для продолжения нажмите ENTER. Для завершения напишите что-нибудь: ')
    if decision:
        return False, 'Спасибо за игру!'
    return True, 'Перезапуск игры...'


def Move(pos, charactrer, field):

    in_row = 3
    pos_x = [2, 0, 1][pos % in_row]
    pos_y = int(pos > in_row) + int(pos > in_row * 2)

    field[pos_y][pos_x] = charactrer

    PrintField(field)
    return field


def NewGame():

    run_game = True

    # Очень страшная штука, но работает правильно
    field = [[1 + j + i + ((i % 3)) * 2 for j in range(3) ] for i in range(3)]

    PrintField(field)
    return run_game, field


def InitGame():
    run_game, field = NewGame()
    is_cell = False

    # print_field(field)

    while run_game:
        while not is_cell:
            cell = int(input('Ходят крестики.\nВведите номер клетки [1-9]: '))
            is_cell = CheckCell(cell, field)

        is_cell = False

        Move(cell, 'X', field)

        if CheckWin(field, 'X'):
            print('Выиграли крестики!!!!')

            run_game, msg = RestartGame()

            print(msg)

            if run_game:
                _, field = NewGame()

            continue

        if not any(CheckCell(cell, field, is_player=False) for cell in range(1,10)):
            print('Ничья!!!!')

            run_game, msg = RestartGame()

            print(msg)

            if run_game:
                _, field = NewGame()

            continue

        while not is_cell:
            cell = int(input('Ходят нолики.\nВведите номер клетки [1-9]: '))
            is_cell = CheckCell(cell, field)

        is_cell = False

        Move(cell, 'O', field)

        if CheckWin(field, 'O'):
            print('Выиграли нолики!!!!')

            run_game, msg = RestartGame()

            print(msg)

            if run_game:
                _, field = NewGame()

            continue

InitGame()