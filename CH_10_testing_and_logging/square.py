def square(n: int) -> int:
    '''
    Returns the input number, squared

    >>> square(2)
    4

    Args:
        n (int): The number to square

    Returns:
        int: The squared result
    '''
    return n * n


if __name__ == '__main__':
    import doctest
    doctest.testmod()

