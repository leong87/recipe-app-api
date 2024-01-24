# recipe-app-api
Recipe API project

Dockerfile 
    #create virtual enviroment
    RUN python -m venv /py &&\   
    #TODO Upgrade de pip (python packague management) on the virtual enviroment just create   
    /py/bin/pip install --upgrade pip && \
    # TODO install list of requiremtns inside the docker images (virtual enviroment)
    /py/bin/pip install -r /tmp/requirements.txt && \
    # TODO  remove  tmp directory, we want to avoid any extra dependencies  ones the images has been created is best practice to keep docker as light weight as posibble
    rm -rf /tmp && \
    # TODO call the add user comands as new user inside our image. its best practice not to use the root user (DONT RUN THE APP USING THE ROOT USER) 
    adduser\
        --disabñed-password\
        --no-create-home \
        django-user

    # UPDATES the enviroment variable inside the image, defines the dir where executables can be run, will run automatic from virtaul enviromen
    ENV PATH="/py/bin:$PATH"

    # TODO util this lines we run as root user umtil it changes to django-user
    USER django-user


FLAKE 8 LINT (will on luy be use for development)

    Command -> docker-compose run app sh -c "flake8"

DOCKER-COMPOSE
# version of the docker compose syntax
version: "3.9"

# Docker compose files consis one or more services needed for the app
services:
  app:
    build:
      #  build the docker file inside the current directory "." mean run in the current directory
      context: .
      args: -DEV:true
  ports:
    - "8000:8000"
  # Mapping the directory from the system to the docker directory
  volumes: -./app:/app
  # By defaul it runs this command from the docker compose
  command: >
    sh -c python manage.py runserver 0.0.0.0:8000