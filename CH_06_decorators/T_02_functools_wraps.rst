>>> def decorator(function):
...    def _decorator(*args, **kwargs):
...        return function(*args, **kwargs)
...    return _decorator

>>> @decorator
... def add(a, b):
...     '''Add a and b'''
...     return a + b

>>> help(add)
Help on function _decorator in module ...:
<BLANKLINE>
_decorator(*args, **kwargs)
<BLANKLINE>

>>> add.__name__
'_decorator'

------------------------------------------------------------------------------

>>> import functools

>>> def decorator(function):
...     @functools.wraps(function)
...     def _decorator(*args, **kwargs):
...         return function(*args, **kwargs)
...     return _decorator

>>> @decorator
... def add(a, b):
...     '''Add a and b'''
...     return a + b

>>> help(add)
Help on function add in module ...:
<BLANKLINE>
add(a, b)
    Add a and b
<BLANKLINE>

>>> add.__name__
'add'
