>>> def generator():
...     yield 1
...     yield 'a'
...     yield []
...     return 'end'

>>> result = generator()

>>> result
<generator object generator at ...>

>>> len(result)
Traceback (most recent call last):
    ...
TypeError: object of type 'generator' has no len()

>>> result[:10]
Traceback (most recent call last):
    ...
TypeError: 'generator' object is not subscriptable

>>> list(result)
[1, 'a', []]

>>> list(result)
[]

------------------------------------------------------------------

>>> def generator_with_return():
...     yield 'some_value'
...     return 'The end of our generator'

>>> result = generator_with_return()
>>> next(result)
'some_value'
>>> next(result)
Traceback (most recent call last):
    ...
StopIteration: The end of our generator

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

