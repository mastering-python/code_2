import pathlib
import setuptools

# Get the current directory
PROJECT_PATH = pathlib.Path(__file__).parent

sum_of_squares = setuptools.Extension('sum_of_squares', sources=[
    # Get the relative path to sum_of_squares.c
    str(PROJECT_PATH / 'sum_of_squares.c'),
])

if __name__ == '__main__':
    setuptools.setup(
        name='SumOfSquares',
        version='1.0',
        ext_modules=[sum_of_squares],
    )

