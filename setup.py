from setuptools import find_packages, setup
from typing import List

# Declaring variable for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHER = "Ashish Patil"
DESCRIPTION = "This is Machine Learning Project for house price prediction"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file. 

    return: This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file. 
    ["Flask", "gunicorn", "pandas", "numpy", "sklearn", "-e ."]
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .") 
    """
    pip install -e . 
    1. It is used to check local packages inside root folder
    2. Here we are going to remove -e . because we have used find_packages() function which
       can perform similar task.
    """



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHER,
    description=DESCRIPTION,
    packages=find_packages(),                    #or ["housing"]   function to find custom packages (housing)
    install_requires=get_requirements_list()     # function to read names of external packages written in requirement.txt file
)

