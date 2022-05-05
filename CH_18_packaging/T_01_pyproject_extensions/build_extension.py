import pathlib
import setuptools

# Get the current directory
PROJECT_PATH = pathlib.Path(__file__).parent

# Create the extension object with the references to the C source
sum_of_squares = setuptools.Extension('sum_of_squares', sources=[
    # Get the relative path to sum_of_squares.c
    str(PROJECT_PATH / 'sum_of_squares.c'),
])


def build(setup_kwargs):
    setup_kwargs['ext_modules'] = [sum_of_squares]
