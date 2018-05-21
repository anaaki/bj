from setuptools import setup, find_packages

setup(
    name='bj',
    version='0.0.1',
    description='black jack game',
    author='naoaki taira',
    author_email='taira@gmail.com',
    url='',
    entry_points = {
        'console_scripts': ['blackjackgame=bj.game:main'],
    },
    packages=find_packages(exclude=('tests')),
    test_suite="tests",
)