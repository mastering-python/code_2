>>> import functools

>>> def add(function=None, add_n=0):
...     # function is not callable so it's probably `add_n`
...     if not callable(function):
...         # Test to make sure we don't pass `None` as `add_n`
...         if function is not None:
...             add_n = function
...         return functools.partial(add, add_n=add_n)
...     
...     @functools.wraps(function)
...     def _add(n):
...         return function(n) + add_n
...
...     return _add

>>> @add
... def add_zero(n):
...     return n

>>> @add(1)
... def add_one(n):
...     return n

>>> @add(add_n=2)
... def add_two(n):
...     return n

>>> add_zero(5)
5

>>> add_one(5)
6

>>> add_two(5)
7
