import setuptools


if __name__ == '__main__':
    setuptools.setup(
        name='T_02_basic_setup_py',
        version='0.1.0',
        packages=setuptools.find_packages(),
        url='https://wol.ph/',
        author='Rick van Hattem',
        author_email='wolph@wol.ph',
        setup_requires=['pytest-runner'],
        install_requires=['portalocker'],
        extras_require={
            'docs': ['sphinx'],
            'tests': ['pytest'],
        },
        entry_points={
            'console_scripts': [
                'our_command = T_02_basic_setup_py.main:run',
            ],
        },
        include_package_data=True,
        package_data={
            # Include all documentation files
            '': ['*.rst'],

            # Include docs and tests
            'tests': ['*'],
            'docs': ['*'],
        },
        exclude_package_data={
            '': ['*.pyc', '*.pyo'],
            'dist': ['*'],
            'build': ['*'],
        },
        project_urls=dict(
            docs='https://progressbar-2.readthedocs.io/',
        ),
    )
