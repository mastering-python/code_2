import typing


def pow(base: int, exponent: int) -> int:
    return base ** exponent


pow(2.5, 10)

################################################################

Username = typing.NewType('Username', str)

rick = Username('Rick')


def print_username(username: Username):
    print(f'Username: {username}')


print_username(rick)
print_username(str(rick))

################################################################

T = typing.TypeVar('T')


def to_string(value: T) -> T:
    return str(value)


to_string(1)
