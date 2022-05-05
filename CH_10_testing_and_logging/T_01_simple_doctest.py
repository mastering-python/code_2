def square(n: int) -> int:
    '''
    >>> square('x')
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for ** or pow(): ...
    '''
    return n ** 2


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

