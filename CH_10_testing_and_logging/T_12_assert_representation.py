class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


def test_user_equal():
    a = User('Rick')
    b = User('Guido')

    assert a == b
