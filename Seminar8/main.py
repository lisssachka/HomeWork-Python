from controller import user_interface

def run():
    decision = ''

    while not decision:
        user_interface()

        decision = input('Для продолжения нажмите ENTER. Для завершения нажмите любую клавишу: ')

if __name__ == '__main__':
    run()