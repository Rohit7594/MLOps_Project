from setuptools import find_packages,setup
from typing import List

hypen_e_dot="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of all requirements
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[lib.replace("/n","") for lib in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements 

setup(
name="MLOps Project",
version="0.0.1",
author="Rohit Saroj",
author_email="rohitsaroj29@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)