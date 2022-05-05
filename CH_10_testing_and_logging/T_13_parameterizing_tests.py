import pytest
import cube


cubes = (
    (0, 0),
    (1, 1),
    (2, 8),
    (3, 27),
)


@pytest.mark.parametrize('n,expected', cubes)
def test_cube(n, expected):
    assert cube.cube(n) == expected

