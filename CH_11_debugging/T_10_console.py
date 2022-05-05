import code


def start_console():
    some_variable = 123
    print(f'Launching console, some_variable: {some_variable}')
    code.interact(banner='console:', local=locals())
    print(f'Exited console, some_variable: {some_variable}')


if __name__ == '__main__':
    start_console()
