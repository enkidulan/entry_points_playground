from setuptools import setup, find_packages

setup(
    name='snake_b',
    version="0.0.1",
    packages=".",
    entry_points={
        'mydomain.myplugin': [
            'install = snake_b:install',
        ],
    }
)