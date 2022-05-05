import pathlib
import setuptools

# Get the current directory
PROJECT_PATH = pathlib.Path(__file__).parent

sum_of_large_squares = setuptools.Extension(
    'sum_of_large_squares',
    sources=[str(PROJECT_PATH / 'sum_of_large_squares.c')])

if __name__ == '__main__':
    setuptools.setup(
        name='SumOfSquares',
        version='1.0',
        ext_modules=[sum_of_large_squares],
    )

