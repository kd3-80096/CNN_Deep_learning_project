

import os  ## Programs that import and use 'os' stand a better chance of being portable between different platforms
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  ## will give us the asctime and message

 ## It will create path based on  systems being used

print(Path("x/y/z.txt"))  ## in windows the path address has forward slash

package_name = "DeepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
     f"src/{package_name}/__init__.py",
     f"src/{package_name}/components/__init__.py",
     f"src/{package_name}/utils/__init__.py",
     f"src/{package_name}/config/__init__.py",
     f"src/{package_name}/pipeline/__init__.py",
     f"src/{package_name}/entity/__init__.py",
     f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",    
    "tests/unit/__init__.py",  ## unit test used for testing specific class or the functions
    "tests/integration/__init__.py",  ## integration testing is used for testing components in pipeline
    "configs/config.yaml",  ## this file contains all our configurations
    "dvc.yaml",   ## For creating the data version control pipeline
    "params.yaml", ## contains the training parameters at one place
    "init_setup.sh",  ## this is shell script file which will hwlp to create the environment
    "requirements.txt",  ## all the required packages and libraries will be here
    "requirements_dev.txt", ## Here it will help us to contain all the development requirements
    "setup.py",  ## 
    "setup.cfg",
    "pyproject.toml",  ## required if we are creating the python packages
    "tox.ini",
    "research/trials.ipynb" ## for trail purpose we will create these files

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)  ## it will return the file-directory and filename 
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)  ## condition to check whether file is present in directory
        logging.info(f"Creating directory: {filedir} for file: {filename}") ##creating the filedirectory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): ##if file doesn't exist or size is 0kb
        with open(filepath,"w") as f: ## create an empty file
            pass  
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exist")



