>>> def square(iterable):
...     for i in iterable:
...         yield i ** 2

>>> list(square(range(5)))
[0, 1, 4, 9, 16]

------------------------------------------------------------------

>>> def padded_square(iterable):
...     yield 'begin'
...     for i in iterable:
...         yield i ** 2
...     yield 'end'

>>> list(padded_square(range(5)))
['begin', 0, 1, 4, 9, 16, 'end']

------------------------------------------------------------------

>>> def lazy():
...     print('before the yield')
...     yield 'yielding'
...     print('after the yield')

>>> generator = lazy()

>>> next(generator)
before the yield
'yielding'

>>> next(generator)
Traceback (most recent call last):
    ...
StopIteration

------------------------------------------------------------------

>>> def lazy():
...     print('before the yield')
...     yield 'yielding'
...     print('after the yield')

>>> generator = lazy()

>>> next(generator)
before the yield
'yielding'

>>> try:
...     next(generator)
... except StopIteration:
...     pass
after the yield

>>> for item in lazy():
...     print(item)
before the yield
yielding
after the yield

------------------------------------------------------------------

>>> import itertools

>>> def odd(iterable):
...     for i in iterable:
...         if i % 2:
...             yield i

>>> def square(iterable):
...     for i in iterable:
...         yield i ** 2

>>> list(square(odd(range(10))))
[1, 9, 25, 49, 81]
