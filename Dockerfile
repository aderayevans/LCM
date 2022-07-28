FROM python:3.9.5-slim-buster

# setup environment variable
ENV DockerHOME=/home/app/webapp

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies  
RUN pip install --upgrade pip  
COPY requirements.txt $DockerHOME
RUN pip install -r requirements.txt

# copy whole project to your docker home directory.
COPY . $DockerHOME
# start server 
CMD [ "python", "manage.py", "runserver", "0:8000" ] # runserver is a django command, 0 is a shortcut for 0.0.0.0.