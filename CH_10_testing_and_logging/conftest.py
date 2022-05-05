import sys
import pathlib

# Little hack to add the current directory to sys.path so we can
# find the imports
path = pathlib.Path(__file__).parent
sys.path.append(str(path.resolve()))


from T_12_assert_representation import User


def is_user(value):
    return isinstance(value, User)


def pytest_assertrepr_compare(config, op, left, right):
    if is_user(left) and is_user(right) and op == '==':
        return [
            'Comparing User instances:',
            f'    name: {left.name} != {right.name}',
        ]

