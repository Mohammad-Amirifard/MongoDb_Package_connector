from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     

Hypen_e_edit = '-e .'
def get_requirement(file_path:str)->List[str]:
    """
    Args:
        file_path: direction of requirement_dev.txt
    Returns:
        List: Return all package names available in the txt file as a list.
    
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        if Hypen_e_edit in requirements:
            requirements.remove(Hypen_e_edit)
    
    return requirements


AUTHOR_NAME = "Mohammad Amirifard"
__version__ = "0.0.4"
REPO_NAME = "MongoDb_Package_connector"
PKG_NAME= "MongoDb_Connector"
AUTHOR_USER_NAME = "Mohammad-Amirifard"
AUTHOR_EMAIL = "Mohammad.Amirifard@mail.polimi.it"


setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirement("./requirements_dev.txt")
     
    )


