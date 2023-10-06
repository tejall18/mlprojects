from setuptools import find_packages,setup  #it will automatically find the packages that are availble in the entire ML application/directry that we have actually created
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        

#this can be considered as the metadata of the entire project
setup(
name ='mlprojects',
version='0.1',
author='Tejal',
author_email='tejalmhatre87@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)