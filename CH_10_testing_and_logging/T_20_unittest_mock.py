from unittest import mock
import random


@mock.patch('random.random')
def test_random(mock_random):
    # Specify our mock return value
    mock_random.return_value = 0.1
    # Test for the mock return value
    assert random.random() == 0.1
    assert mock_random.call_count == 1


def test_random_with():
    with mock.patch('random.random') as mock_random:
        mock_random.return_value = 0.1
        assert random.random() == 0.1

##############################################################################


import os
from unittest import mock


def delete_file(filename):
    while os.path.exists(filename):
        os.unlink(filename)


@mock.patch('os.path.exists', side_effect=(True, False, False))
@mock.patch('os.unlink')
def test_delete_file(mock_exists, mock_unlink):
    # First try:
    delete_file('some non-existing file')

    # Second try:
    delete_file('some non-existing file')
