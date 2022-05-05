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
        name='T_04_C_extensions',
        version='0.1.0',
        packages=setuptools.find_packages(),
        url='https://wol.ph/',
        author='Rick van Hattem',
        author_email='wolph@wol.ph',
        ext_modules=[sum_of_squares],
    )
