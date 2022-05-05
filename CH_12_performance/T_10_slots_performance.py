import timeit
import pytest
import functools


class WithSlots:
    __slots__ = 'eggs',


class WithoutSlots:
    pass


with_slots = WithSlots()
no_slots = WithoutSlots()


@pytest.mark.skip()
def test_set(obj):
    obj.eggs = 5


@pytest.mark.skip()
def test_get(obj):
    return obj.eggs


timer = functools.partial(
    timeit.timeit,
    number=20000000,
    setup='\n'.join((
        f'from {__name__} import with_slots, no_slots',
        f'from {__name__} import test_get, test_set',
    )),
)
for function in 'test_set', 'test_get':
    print(function)
    print('with slots', timer(f'{function}(with_slots)'))
    print('with slots', timer(f'{function}(no_slots)'))
