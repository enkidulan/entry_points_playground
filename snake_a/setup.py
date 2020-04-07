from setuptools import setup

setup(
    name='snake_a',
    version="0.0.1",
    packages=".",
    entry_points={
        'mydomain.myplugin': [
            'install = snake_a:install',
        ],
    }
)