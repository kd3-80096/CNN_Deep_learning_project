## A file with .sh extension is a scripting language commands file that contains computer program to be run by Unix shell. It can contain a series of commands that run sequentially to carry out operations such as files processing, execution of programs and other such tasks. These are executed from the command line interface by user or in batch to carry out multiple operations at the same time. 
## Run this in the git bash terminal only


echo [$(date)]: "START" 
echo [$(date)]: "creating env with python 3.8 version" 
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating the environment" 
source activate ./env
echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt
echo [$(date)]: "END" 



