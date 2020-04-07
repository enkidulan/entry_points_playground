from setuptools import setup, find_packages

setup(
    name='snake_e',
    version="0.0.1",
    install_requires=[
        'snake_b',
        'snake_d',
    ],
    packages=".",
    entry_points={
        'mydomain.myplugin': [
            'install = snake_e:install',
        ],
    }
)