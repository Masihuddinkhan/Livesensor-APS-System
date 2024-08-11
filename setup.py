from setuptools import find_packages, setup
#from typing import List

def get_requirements()->list[str]:
    
    requirements_list = list[str] =[]
    
    return requirements_list







setup(
    name = 'senser',
    version="0.0.1",
    auther="masihuddin",
    author_email="masihuddinkhan025@gmai.com",
    packages= find_packages(),
    install_requires = get_requirements(), # ["pymongo"]
    
)