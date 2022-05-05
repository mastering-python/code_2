import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name='T_05_cython',
        version='0.1.0',
        ext_modules=[
            setuptools.Extension(
                'sum_of_squares',
                sources=['T_05_cython/sum_of_squares.pyx'],
            ),
        ],
        setup_requires=['cython'],
    )
