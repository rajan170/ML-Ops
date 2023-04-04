# from pip._internal import req
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    Returns a list of required packages
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [x.replace("\n", "") for x in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ML-Project",
    version='0.0.1',
    author="Rajan",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)