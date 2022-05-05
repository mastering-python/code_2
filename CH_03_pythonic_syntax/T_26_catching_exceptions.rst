>>> exception = None

>>> try:
...     1 / 0
... except ZeroDivisionError as exception:
...     pass

>>> exception
Traceback (most recent call last):
    ...
NameError: name 'exception' is not defined


>>> try:
...     1 / 0
... except ZeroDivisionError as exception:
...     new_exception = exception

>>> new_exception
ZeroDivisionError('division by zero')
