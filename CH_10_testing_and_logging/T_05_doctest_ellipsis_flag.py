'''
>>> {10: 'a', 20: 'b'}  # doctest: +ELLIPSIS
{...}
>>> [True, 1, 'a']  # doctest: +ELLIPSIS
[...]
>>> True,  # doctest: +ELLIPSIS
(...)
>>> [1, 2, 3, 4]  # doctest: +ELLIPSIS
[1, ..., 4]
>>> [1, 0, 0, 0, 0, 0, 4]  # doctest: +ELLIPSIS
[1, ..., 4]

------------------------------------------------------------------------------

>>> class Spam(object):
...     pass
>>> Spam()  # doctest: +ELLIPSIS
<...Spam object at 0x...>
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()

