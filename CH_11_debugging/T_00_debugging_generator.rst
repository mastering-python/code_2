>>> def hiding_generator():
...     print('a')
...     yield 'first value'
...     print('b')
...     yield 'second value'
...     print('c')

>>> generator = hiding_generator()

>>> next(generator)
a
'first value'

>>> next(generator)
b
'second value'

>>> next(generator)
Traceback (most recent call last):
...
StopIteration

##############################################################################

>>> import os
>>> import inspect
>>> import linecache


>>> def print_code():
...     while True:
...         info = inspect.stack()[1]
...         lineno = info.lineno + 1
...         function = info.function
...         # Fetch the next line of code
...         code = linecache.getline(info.filename, lineno)
...         print(f'{lineno:03d} {function}: {code.strip()}')
...         yield


# Always prime the generator

>>> print_code = print_code()


>>> def some_test_function(a, b):
...     next(print_code)
...     c = a + b
...     next(print_code)
...     return c

>>> some_test_function('a', 'b')
003 some_test_function: c = a + b
005 some_test_function: return c
'ab'

