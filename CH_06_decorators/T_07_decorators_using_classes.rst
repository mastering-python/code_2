>>> import functools

>>> class Debug(object):
...
...     def __init__(self, function):
...         self.function = function
...         # functools.wraps for classes
...         functools.update_wrapper(self, function)
...
...     def __call__(self, *args, **kwargs):
...         output = self.function(*args, **kwargs)
...         name = self.function.__name__
...         print(f'{name}({args!r}, {kwargs!r}): {output!r}')
...         return output


>>> @Debug
... def add(a, b=0):
...     return a + b
...
>>> output = add(3)
add((3,), {}): 3

>>> output = add(a=4, b=2)
add((), {'a': 4, 'b': 2}): 6
