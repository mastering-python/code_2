>>> g = 1
>>> def print_global():
...     print(f'Value: {g}')

>>> print_global()
Value: 1

>>> g = 1

>>> def print_global():
...     g += 1
...     print(f'Value: {g}')

>>> print_global()
Traceback (most recent call last):
    ...
UnboundLocalError: local variable 'g' referenced before assignment

