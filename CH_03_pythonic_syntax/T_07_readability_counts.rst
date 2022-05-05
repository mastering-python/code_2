>>> from functools import reduce

>>> fib=lambda n:n if n<2 else fib(n-1)+fib(n-2)
>>> fib(10)
55

>>> fib=lambda n:reduce(lambda x,y:(x[0]+x[1],x[0]),[(1,1)]*(n-1))[0]
>>> fib(10)
55


>>> def fib(n):
...     if n < 2:
...         return n
...     else:
...         return fib(n - 1) + fib(n - 2)

>>> fib(10)
55


>>> def fib(n):
...     a = 0
...     b = 1
...     for _ in range(n):
...         a, b = b, a + b
...
...     return a

>>> fib(10)
55

