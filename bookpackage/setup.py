from setuptools import setup

setup(
    name = 'bookpackage',
    version = '0.1.0',
    author = 'An Awesome Coder',
    author_email = 'aac@example.com',
    description = 'An awesome package that does something'
    packages = find_packages()
    install_requires = ['pandas >= 2.0.3']
)

