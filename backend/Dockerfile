# base image
FROM python:3.11.4-slim-buster

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

# Install necessary system libraries
RUN apt-get update \
    && apt-get install -y libx11-6 libgl1-mesa-glx libxrender1 libfontconfig1 rsync \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# copy whole project to your docker home directory.
COPY ./backend $DockerHOME

# Install application dependencies
RUN pip install -r ./requirements.txt

# Run Django migrations
RUN python ./manage.py makemigrations
RUN python ./manage.py migrate

# Check if there is any user in the database
RUN python load_data.py

# port where the Django app runs
EXPOSE 8000

# start server using Gunicorn
CMD python manage.py runserver 0.0.0.0:8000


# To build -> docker build -t my-django-app .
# To run -> docker run -p 8000:8000 my-django-app