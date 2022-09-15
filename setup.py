## setup.py is a python file, the presence of which is an indication that the module/package you are about to install has likely been packaged and distributed with Distutils, which is the standard for distributing Python Modules.

import setuptools  ## to setup all the tools

with open("README.md", "r", encoding="utf-8") as f:   ## it will read all the discription from readme file
    long_description = f.read()

__version__ = "0.0.0"      ## version we need to give to it

REPO_NAME = "CNN_Deep_learning_project"   ## git repository name
AUTHOR_USER_NAME = "deveshpatil619"          ## git author name
SRC_REPO = "DeepClassifier"                     ## project name
AUTHOR_EMAIL = "deveshpatil619@gmail.com"       ## email

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,  ## It will come from the readme file
    long_description_content="text/markdown", ## type of it
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},   ## in src folder we need to find the packages
    packages=setuptools.find_packages(where="src")
)
