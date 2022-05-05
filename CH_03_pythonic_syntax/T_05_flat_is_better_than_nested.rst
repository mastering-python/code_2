>>> def between_and_modulo(value, a, b, modulo):
...     if value >= a:
...         if value <= b:
...             if value % modulo:
...                 return True
...     return False

>>> for i in range(10):
...     if between_and_modulo(i, 2, 9, 2):
...         print(i, end=' ')
3 5 7 9


>>> def between_and_modulo(value, a, b, modulo):
...     if value < a:
...         return False
...     elif value > b:
...         return False
...     elif not value % modulo:
...         return False
...     else:
...         return True

>>> for i in range(10):
...     if between_and_modulo(i, 2, 9, 2):
...         print(i, end=' ')
3 5 7 9
