import pytest
import cube_root


cubes = (
    (0, 0),
    (1, 1),
    (8, 2),
    (27, 3),
)


@pytest.mark.parametrize('n,expected', cubes)
def test_cube_root(n, expected):
    assert cube_root.cube_root(n) == expected


def test_cube_root_below_zero():
    with pytest.raises(ValueError):
        cube_root.cube_root(-1)

