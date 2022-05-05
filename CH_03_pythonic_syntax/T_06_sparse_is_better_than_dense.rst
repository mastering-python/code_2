>>> f=lambda x:0**x or x*f(x-1)
>>> f(40)
815915283247897734345611269596115894272000000000

>>> def factorial(x):
...     if 0 ** x:
...         return 1
...     else:
...         return x * factorial(x - 1)
>>> factorial(40)
815915283247897734345611269596115894272000000000
