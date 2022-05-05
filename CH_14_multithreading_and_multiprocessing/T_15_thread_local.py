import threading
import concurrent.futures


context = threading.local()


def init_counter():
    context.counter = 10


def increment(name):
    current_value = context.counter
    print(f'{name} value before increment: {current_value}')
    context.counter = current_value + 1
    print(f'{name} value after increment: {context.counter}')


init_counter()
print(f'Before thread start: {context.counter}')

with concurrent.futures.ThreadPoolExecutor(
        initializer=init_counter) as executor:
    executor.map(increment, range(5))

print(f'After thread finish: {context.counter}')
