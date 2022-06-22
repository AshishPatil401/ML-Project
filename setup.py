from setuptools import setup
from typing import List

#Declaring variable for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHER = "Ashish Patil"
DESCRIPTION = "This is Machine Learning Project for house price prediction"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file. 

    return: This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file. 
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHER,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)

