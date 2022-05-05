from . import a


class B(a.A):

    def regular_method(self):
        '''This regular method overrides
        :meth:`a.A.regular_method`
        '''
        pass

