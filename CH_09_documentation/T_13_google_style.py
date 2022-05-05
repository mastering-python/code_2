class Eggs:
    pass


class Spam(object):

    r'''
    The Spam object contains lots of spam

    Args:
        arg: The arg is used for ...
        \*args: The variable arguments are used for ...
        \*\*kwargs: The keyword arguments are used for ...

    Attributes:
        arg: This is where we store arg,
    '''

    def __init__(self, arg: str, *args, **kwargs):
        self.arg: str = arg

    def eggs(self, number: int, cooked: bool) -> Eggs:
        '''We can't have spam without eggs, so here are the eggs

        Args:
            number: The number of eggs to return
            cooked: Should the eggs be cooked?

        Raises:
            RuntimeError: Out of eggs

        Returns:
            Eggs: A bunch of eggs
        '''
        pass

