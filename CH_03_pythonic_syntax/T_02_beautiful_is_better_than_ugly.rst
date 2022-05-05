>>> filter_modulo = lambda i, m: (i[j] for j in \
...                               range(len(i)) if i[j] % m)
>>> list(filter_modulo(range(10), 2))
[1, 3, 5, 7, 9]


>>> def filter_modulo(items, modulo):
...     for item in items:
...         if item % modulo:
...             yield item
...

>>> list(filter_modulo(range(10), 2))
[1, 3, 5, 7, 9]
