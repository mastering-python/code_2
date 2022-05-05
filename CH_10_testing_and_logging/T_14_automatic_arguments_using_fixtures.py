##################################################################

import pytest


@pytest.fixture
def name():
    return 'Rick'


def test_something(name):
    assert name == 'Rick'


##################################################################

def test_cache(cache):
    counter = cache.get('counter', 0) + 1
    assert counter
    cache.set('counter', counter)

##################################################################


import pytest


@pytest.fixture
def some_yield_fixture():
    with open(__file__ + '.txt', 'w') as fh:
        # Before the function
        yield fh
        # After the function


@pytest.fixture
def some_regular_fixture():
    # Do something here
    return 'some_value_to_pass_as_parameter'


def some_test(some_yield_fixture, some_regular_fixture):
    some_yield_fixture.write(some_regular_fixture)


##################################################################


import pytest
import sqlite3


@pytest.fixture(params=[':memory:'])
def connection(request):
    return sqlite3.connect(request.param)


@pytest.yield_fixture
def transaction(connection):
    with connection:
        yield connection


def test_insert(transaction):
    transaction.execute('create table test (id integer)')
    for i in range(3):
        transaction.execute('insert into test values (?)', (i,))

