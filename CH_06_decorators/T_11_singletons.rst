>>> import functools

>>> def singleton(cls):
...     instances = dict()
...     @functools.wraps(cls)
...     def _singleton(*args, **kwargs):
...         if cls not in instances:
...             instances[cls] = cls(*args, **kwargs)
...         return instances[cls]
...     return _singleton

>>> @singleton
... class SomeSingleton(object):
...     def __init__(self):
...         print('Executing init')

>>> a = SomeSingleton()
Executing init
>>> b = SomeSingleton()

>>> a is b
True

>>> a.x = 123
>>> b.x
123
