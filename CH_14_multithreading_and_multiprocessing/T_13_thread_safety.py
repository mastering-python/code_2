import concurrent.futures


counter = 10


def increment(name):
    global counter
    current_value = counter
    print(f'{name} value before increment: {current_value}')
    counter = current_value + 1
    print(f'{name} value after increment: {counter}')


if __name__ == '__main__':
    print(f'Before thread start: {counter}')

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(increment, range(5))

    print(f'After thread finish: {counter}')
