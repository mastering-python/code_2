>>> import functools

>>> class Value(object):
...     def __init__(self, value):
...         self.value = value
...
...     def __repr__(self):
...         return f'<{self.__class__.__name__} {self.value}>'


>>> class Spam(Value):
...     def __gt__(self, other):
...         return self.value > other.value
...
...     def __ge__(self, other):
...         return self.value >= other.value
...
...     def __lt__(self, other):
...         return self.value < other.value
...
...     def __le__(self, other):
...         return self.value <= other.value
...
...     def __eq__(self, other):
...         return self.value == other.value

>>> @functools.total_ordering
... class Egg(Value):
...     def __lt__(self, other):
...         return self.value < other.value
...
...     def __eq__(self, other):
...         return self.value == other.value

-----------------------------------------------------------------

>>> numbers = [4, 2, 3, 4]
>>> spams = [Spam(n) for n in numbers]
>>> eggs = [Egg(n) for n in numbers]

>>> spams
[<Spam 4>, <Spam 2>, <Spam 3>, <Spam 4>]

>>> eggs
[<Egg 4>, <Egg 2>, <Egg 3>, <Egg 4>]

>>> sorted(spams)
[<Spam 2>, <Spam 3>, <Spam 4>, <Spam 4>]

>>> sorted(eggs)
[<Egg 2>, <Egg 3>, <Egg 4>, <Egg 4>]

# Sorting using key is of course still possible and in this case
perhaps just as easy:

>>> values = [Value(n) for n in numbers]
>>> values
[<Value 4>, <Value 2>, <Value 3>, <Value 4>]

>>> sorted(values, key=lambda v: v.value)
[<Value 2>, <Value 3>, <Value 4>, <Value 4>]

------------------------------------------------------------------------------

>>> def sort_by_attribute(attr, keyfunc=getattr):
...     def _sort_by_attribute(cls):
...         def __lt__(self, other):
...             return getattr(self, attr) < getattr(other, attr)
...
...         def __eq__(self, other):
...             return getattr(self, attr) <= getattr(other, attr)
...
...         cls.__lt__ = __lt__
...         cls.__eq__ = __eq__
...
...         return functools.total_ordering(cls)
...     return _sort_by_attribute

>>> class Value(object):
...     def __init__(self, value):
...         self.value = value
...
...     def __repr__(self):
...         return f'<{self.__class__.__name__} {self.value}>'

>>> @sort_by_attribute('value')
... class Spam(Value):
...     pass

>>> numbers = [4, 2, 3, 4]
>>> spams = [Spam(n) for n in numbers]
>>> sorted(spams)
[<Spam 2>, <Spam 3>, <Spam 4>, <Spam 4>]
