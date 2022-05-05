class Eggs:
    pass


class Spam(object):

    r'''
    The Spam object contains lots of spam

    Parameters
    ----------
    arg : str
        The arg is used for ...
    \*args
        The variable arguments are used for ...
    \*\*kwargs
        The keyword arguments are used for ...

    Attributes
    ----------
    arg : str
        This is where we store arg,
    '''

    def __init__(self, arg, *args, **kwargs):
        self.arg = arg

    def eggs(self, number, cooked):
        '''We can't have spam without eggs, so here are the eggs

        Parameters
        ----------
        number : int
            The number of eggs to return
        cooked : bool
            Should the eggs be cooked?

        Raises
        ------
        RuntimeError
            Out of eggs

        Returns
        -------
        Eggs
            A bunch of eggs
        '''
        pass

