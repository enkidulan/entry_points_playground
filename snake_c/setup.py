from setuptools import setup, find_packages

setup(
    name='snake_c',    
    version="0.0.1",
    packages=".",
    entry_points={
        'mydomain.myplugin': [
            'install = snake_c:install',
        ],
    }
)