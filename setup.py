
from setuptools import find_packages, setup
setup(
    url='https://github.com/getdozer/dozer-python',
    packages=find_packages(exclude=['tests', 'tests.*']),
)
