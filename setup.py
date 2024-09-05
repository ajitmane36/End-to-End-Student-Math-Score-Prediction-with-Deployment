from setuptools import find_packages, setup
from typing import List

def get_requirnments(file_path:str)->List[str]:
    '''This function will return list of requirnments'''
    requirnments=[]
    
    with open(file_path) as file_obj: # Open file path
        requirnments=file_obj.readlines() # Read each line in file
        requirnments=[req.replace('\n','') for req in requirnments] # Replace blank once line end by \n
        
    return requirnments

setup(
    name='mlproject',
    version='0.0.1',
    author='Ajit Mane',
    author_email='ajitmne36@gmail.com',
    packages=find_packages(),
    install_requires=get_requirnments('requirements.txt')
)