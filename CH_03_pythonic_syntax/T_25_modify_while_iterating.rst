>>> dict_ = dict(a=123)
>>> set_ = set((456,))

>>> for key in dict_:
...     del dict_[key]
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration

>>> for item in set_:
...     set_.remove(item)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Set changed size during iteration


>>> list_ = list(range(10))
>>> list_
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> for item in list_:
...     print(list_.pop(0), end=', ')
0, 1, 2, 3, 4,

>>> list_
[5, 6, 7, 8, 9]


>>> list_ = list(range(10))

>>> for item in list(list_):
...     print(list_.pop(0), end=', ')
0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
