import os
import inspect
import linecache


def print_code():
    while True:
        info = inspect.stack()[1]
        lineno = info.lineno
        function = info.function
        # Strip the path from the filename
        filename = os.path.split(info.filename)[-1]
        # Fetch the next line of code
        code = linecache.getline(info.filename, lineno + 1)
        print(f'{filename}:{lineno}:{function}: {code.strip()}')
        yield


# Always prime the generator
print_code = print_code()


def some_test_function(a, b):
    next(print_code)
    c = a + b
    next(print_code)
    return c


some_test_function('a', 'b')
