>>> a = 1
>>> a == True
True
>>> a is True
False

>>> b = 0
>>> b == False
True
>>> b is False
False

>>> def some_unsafe_function(arg=None):
...     if not arg:
...         arg = 123
...
...     return arg

>>> some_unsafe_function(0)
123
>>> some_unsafe_function(None)
123


>>> def some_safe_function(arg=None):
...     if arg is None:
...         arg = 123
...
...     return arg

>>> some_safe_function(0)
0
>>> some_safe_function(None)
123


>>> a = 200 + 56
>>> b = 256
>>> c = 200 + 57
>>> d = 257

>>> a == b
True
>>> a is b
True
>>> c == d
True
>>> c is d
False


>>> spam = list(range(1000000))
>>> eggs = list(range(1000000))

>>> spam == eggs
True
>>> spam is eggs
False
