>>> import functools


>>> def plus_one(function):
...     @functools.wraps(function)
...     def _plus_one(self, n, *args):
...         return function(self, n + 1, *args)
...     return _plus_one


>>> class Adder(object):
...     @plus_one
...     def add(self, a, b=0):
...         return a + b


>>> adder = Adder()
>>> adder.add(0)
1
>>> adder.add(3, 4)
8
