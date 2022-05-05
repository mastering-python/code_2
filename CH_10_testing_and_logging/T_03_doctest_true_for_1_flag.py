'''
>>> False
0
>>> True
1
'''

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testmod(optionflags=doctest.DONT_ACCEPT_TRUE_FOR_1)
