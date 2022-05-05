>>> import bisect

Using the regular sort:
>>> sorted_list = []
>>> sorted_list.append(5)  # O(1)

>>> sorted_list.append(3)  # O(1)

>>> sorted_list.append(1)  # O(1)

>>> sorted_list.append(2)  # O(1)

>>> sorted_list.sort()  # O(n * log(n)) = 4 * log(4) = 8

>>> sorted_list
[1, 2, 3, 5]

Using bisect:
>>> sorted_list = []
>>> bisect.insort(sorted_list, 5)  # O(n) = 1

>>> bisect.insort(sorted_list, 3)  # O(n) = 2

>>> bisect.insort(sorted_list, 1)  # O(n) = 3

>>> bisect.insort(sorted_list, 2)  # O(n) = 4

>>> sorted_list
[1, 2, 3, 5]

------------------------------------------------------------------------------

>>> sorted_list = [1, 2, 5]
>>> def contains(sorted_list, value):
...     for item in sorted_list:
...         if item > value:
...             break
...         elif item == value:
...             return True
...     return False

>>> contains(sorted_list, 2)  # Need to walk through 2 items, O(n) = 2
True
>>> contains(sorted_list, 4)  # Need to walk through n items, O(n) = 3
False
>>> contains(sorted_list, 6)  # Need to walk through n items, O(n) = 3
False


>>> import bisect

>>> sorted_list = [1, 2, 5]
>>> def contains(sorted_list, value):
...     i = bisect.bisect_left(sorted_list, value)
...     return i < len(sorted_list) and sorted_list[i] == value

>>> contains(sorted_list, 2)  # Found it the first step, O(log(n)) = 1
True
>>> contains(sorted_list, 4)  # No result after 2 steps, O(log(n)) = 2
False
>>> contains(sorted_list, 6)  # No result after 2 steps, O(log(n)) = 2
False


>>> import bisect
>>> import collections

>>> class SortedList:
...     def __init__(self, *values):
...         self._list = sorted(values)
...     
...     def index(self, value):
...         i = bisect.bisect_left(self._list, value)
...         if i < len(self._list) and self._list[i] == value:
...             return index
...
...     def delete(self, value):
...         del self._list[self.index(value)]
...
...     def add(self, value):
...         bisect.insort(self._list, value)
...
...     def __iter__(self):
...         for value in self._list:
...             yield value
...
...     def __exists__(self, value):
...         return self.index(value) is not None

>>> sorted_list = SortedList(1, 3, 6, 2)
>>> 3 in sorted_list
True
>>> 5 in sorted_list
False
>>> sorted_list.add(5)
>>> 5 in sorted_list
True
>>> list(sorted_list)
[1, 2, 3, 5, 6]
