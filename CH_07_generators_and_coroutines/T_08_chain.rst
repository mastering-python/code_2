>>> def chain(*iterables):
...     for iterable in iterables:
...         yield from iterable

>>> a = 1, 2, 3
>>> b = [4, 5, 6]
>>> c = 'abc'
>>> list(chain(a, b, c))
[1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

>>> a + b + c
Traceback (most recent call last):
    ...
TypeError: can only concatenate tuple (not "list") to tuple

------------------------------------------------------------------

>>> def chain(*iterables):
...     for iterable in iterables:
...         for i in iterable:
...             yield i

