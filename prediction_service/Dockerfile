FROM python:3.8-slim  
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]

# python:3.8-slim means the light weight version of the python
#  inside the container we are building the working directory in above case in root folder app will be created
# copy .. means copy all files present into prediction service and paste into the working directory
# run will install all the requirements
#  cmd will always run the commands in it whenever we will run the dockers