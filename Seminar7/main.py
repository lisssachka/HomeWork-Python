from controller import user_interface

def run():
    button = ''

    while not button:
        user_interface()
        button = input('Для продолжения ENTER. Для завершения любую клавишу: ')

if __name__ == '__main__':
    run()