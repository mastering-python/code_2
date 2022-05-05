def square(n: int) -> int:
    '''
    Returns the input number, squared

    >>> square(0)
    0
    >>> square(1)
    1
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square()
    Traceback (most recent call last):
    ...
    TypeError: square() missing 1 required positional argument: 'n'
    >>> square('x')
    Traceback (most recent call last):
    ...
    TypeError: can't multiply sequence by non-int of type 'str'

    Args:
        n (int): The number to square

    Returns:
        int: The squared result
    '''
    return n * n


if __name__ == '__main__':
    import doctest
    doctest.testmod()

