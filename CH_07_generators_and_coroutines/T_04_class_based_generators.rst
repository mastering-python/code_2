>>> class CountGenerator:
...     def __init__(self, start=0, step=1, stop=None):
...         self.start = start
...         self.step = step
...         self.stop = stop
...
...     def __iter__(self):
...         i = self.start
...         while self.stop is None or i < self.stop:
...             yield i
...             i += self.step

>>> list(CountGenerator(start=2.5, step=0.5, stop=5))
[2.5, 3.0, 3.5, 4.0, 4.5]

------------------------------------------------------------------

>>> class CountIterator:
...     def __init__(self, start=0, step=1, stop=None):
...         self.i = start
...         self.start = start
...         self.step = step
...         self.stop = stop
...
...     def __iter__(self):
...         return self
...
...     def __next__(self):
...         if self.stop is not None and self.i >= self.stop:
...             raise StopIteration
...
...         # we need to return the value before we increment to
...         # maintain identical behavior
...         value = self.i
...         self.i += self.step
...         return value

>>> list(CountIterator(start=2.5, step=0.5, stop=5))
[2.5, 3.0, 3.5, 4.0, 4.5]

------------------------------------------------------------------

>>> import itertools

>>> class AdvancedCountIterator:
...     def __init__(self, start=0, step=1, stop=None):
...         self.i = start
...         self.start = start
...         self.step = step
...         self.stop = stop
...
...     def __iter__(self):
...         return self
...
...     def __next__(self):
...         if self.stop is not None and self.i >= self.stop:
...             raise StopIteration
...
...         value = self.i
...         self.i += self.step
...         return value
...
...     def __len__(self):
...         return int((self.stop - self.start) // self.step)
...
...     def __contains__(self, key):
...         # To check `if 123 in count`.
...         # Note that this does not look at `step`!
...         return self.start < key < self.stop
...
...     def __repr__(self):
...         return (
...             f'{self.__class__.__name__}(start={self.start}, '
...             f'step={self.step}, stop={self.stop})')
...
...     def __getitem__(self, slice_):
...         return itertools.islice(self, slice_.start,
...                                 slice_.stop, slice_.step)

>>> count = AdvancedCountIterator(start=2.5, step=0.5, stop=5)

# Pretty representation using `__repr__`

>>> count
AdvancedCountIterator(start=2.5, step=0.5, stop=5)

# Check if item exists using `__contains__`

>>> 3 in count
True
>>> 3.1 in count
True
>>> 1 in count
False

# Getting the length using `__len__`

>>> len(count)
5

# Slicing using `__getitem__` with a slice as a parameter

>>> count[:3]
<itertools.islice object at 0x...>

>>> list(count[:3])
[2.5, 3.0, 3.5]

>>> list(count[:3])
[4.0, 4.5]

