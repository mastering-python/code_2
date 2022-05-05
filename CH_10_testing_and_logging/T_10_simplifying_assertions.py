import unittest
import cube

n = 2
expected = 8


# Regular unit test
class TestCube(unittest.TestCase):

    def test_2(self):
        self.assertEqual(cube.cube(n), expected)

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            cube.cube()


# py.test class
class TestPyCube:

    def test_2(self):
        assert cube.cube(n) == expected


# py.test functions
def test_2():
    assert cube.cube(n) == expected

