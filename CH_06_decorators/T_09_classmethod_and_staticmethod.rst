>>> import pprint


>>> class Spam(object):
...
...     def some_instancemethod(self, *args, **kwargs):
...         pprint.pprint(locals(), width=60)
...
...     @classmethod
...     def some_classmethod(cls, *args, **kwargs):
...         pprint.pprint(locals(), width=60)
...
...     @staticmethod
...     def some_staticmethod(*args, **kwargs):
...         pprint.pprint(locals(), width=60)

# Create an instance so we can compare the difference between
executions with and without instances easily

>>> spam = Spam()

------------------------------------------------------------------------------

# With an instance (note the lowercase spam)

>>> spam.some_instancemethod(1, 2, a=3, b=4)
{'args': (1, 2),
 'kwargs': {'a': 3, 'b': 4},
 'self': <__main__.Spam object at ...>}

# Without an instance (note the capitalized Spam)

>>> Spam.some_instancemethod()
Traceback (most recent call last):
    ...
TypeError: ...some_instancemethod() missing ... argument: 'self'

# But what if we add parameters? Be very careful with these!
Our first argument is now used as an argument, this can give
very strange and unexpected errors

>>> Spam.some_instancemethod(1, 2, a=3, b=4)
{'args': (2,), 'kwargs': {'a': 3, 'b': 4}, 'self': 1}

------------------------------------------------------------------------------

# Classmethods are expectedly identical

>>> spam.some_classmethod(1, 2, a=3, b=4)
{'args': (1, 2),
 'cls': <class '__main__.Spam'>,
 'kwargs': {'a': 3, 'b': 4}}

>>> Spam.some_classmethod()
{'args': (), 'cls': <class '__main__.Spam'>, 'kwargs': {}}

>>> Spam.some_classmethod(1, 2, a=3, b=4)
{'args': (1, 2),
 'cls': <class '__main__.Spam'>,
 'kwargs': {'a': 3, 'b': 4}}

------------------------------------------------------------------------------

# Staticmethods are also identical

>>> spam.some_staticmethod(1, 2, a=3, b=4)
{'args': (1, 2), 'kwargs': {'a': 3, 'b': 4}}

>>> Spam.some_staticmethod()
{'args': (), 'kwargs': {}}

>>> Spam.some_staticmethod(1, 2, a=3, b=4)
{'args': (1, 2), 'kwargs': {'a': 3, 'b': 4}}

------------------------------------------------------------------------------

>>> class Spam:
...
...     def __init__(self, spam=1):
...         self.spam = spam
...
...     def __get__(self, instance, cls):
...         return self.spam + instance.eggs
...
...     def __set__(self, instance, value):
...         instance.eggs = value - self.spam

>>> class Sandwich:
...
...     spam = Spam(5)
...
...     def __init__(self, eggs):
...         self.eggs = eggs

>>> sandwich = Sandwich(1)
>>> sandwich.eggs
1
>>> sandwich.spam
6

>>> sandwich.eggs = 10
>>> sandwich.spam
15

------------------------------------------------------------------------------

>>> import functools

>>> class ClassMethod(object):
...     def __init__(self, method):
...         self.method = method
... 
...     def __get__(self, instance, cls):
...         @functools.wraps(self.method)
...         def method(*args, **kwargs):
...             return self.method(cls, *args, **kwargs)
...         return method

>>> class StaticMethod(object):
...     def __init__(self, method):
...         self.method = method
... 
...     def __get__(self, instance, cls):
...         return self.method

>>> class Sandwich:
...     spam = 'class'
...
...     def __init__(self, spam):
...         self.spam = spam
...
...     @ClassMethod
...     def some_classmethod(cls, arg):
...         return cls.spam, arg
...
...     @StaticMethod
...     def some_staticmethod(arg):
...         return Sandwich.spam, arg

>>> sandwich = Sandwich('instance')
>>> sandwich.spam
'instance'
>>> sandwich.some_classmethod('argument')
('class', 'argument')
>>> sandwich.some_staticmethod('argument')
('class', 'argument')
