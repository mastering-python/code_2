class A(object):

    def __init__(self, arg, *args, **kwargs):
        pass

    def regular_method(self, arg):
        pass

    @classmethod
    def decorated_method(self, arg):
        pass

    def _hidden_method(self):
        pass

