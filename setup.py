from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of required libraries
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

setup(
    name="car price prediction project",
    version="0.0.1",
    author="ST",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)