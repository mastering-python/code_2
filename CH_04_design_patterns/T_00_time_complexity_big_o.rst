>>> n = 1000
>>> a = list(range(n))
>>> b = dict.fromkeys(range(n))
>>> for i in range(100):
...     assert i in a  # takes n=1000 steps
...     assert i in b  # takes 1 step


>>> def o_one(items):
...     return 1  # 1 operation so O(1)

>>> def o_n(items):
...     total = 0
...     # Walks through all items once so O(n)
...     for item in items:
...         total += item
...     return total

>>> def o_n_squared(items):
...     total = 0
...     # Walks through all items n*n times so O(n**2)
...     for a in items:
...         for b in items:
...             total += a * b
...     return total

>>> n = 10
>>> items = range(n)
>>> o_one(items)  # 1 operation
1
>>> o_n(items)  # n = 10 operations
45
>>> o_n_squared(items)  # n*n = 10*10 = 100 operations
2025
