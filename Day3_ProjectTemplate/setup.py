from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "Machine Learning project"
VERSION = "0.0.1"
AUTHOR = "Manpreet Singh"
DESCRIPTION = "This is our Machine learning project"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPEN_E_DOT = "-e ."



def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)


        return requirement_list



setup(
    name = PROJECT_NAME,
    version = VERSION,
    author  = AUTHOR,
    description= DESCRIPTION,
    packages = find_packages(),
    install_requires = get_requirements_list()

         
)
