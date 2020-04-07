from setuptools import setup, find_packages

setup(
    name='snake_d',
    version="0.0.1",
    install_requires=[
        'snake_a',
        'snake_c',
    ],
    packages=".",
    entry_points={
        'mydomain.myplugin': [
            'install = snake_d:install',
        ],
    }
)