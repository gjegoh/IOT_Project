# IOT Project - Diabreezy

## Project Description
App to help patients suffering from diabetes

## Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
    - Has support for Windows and MacOS
- Clone this repo:
~~~
$ git git@github.com:gjegoh/IOT_Project.git
$ cd IOT_Project
~~~

## Steps to Running the Project
- If running the project for the first time, build and start the container:
~~~
$ docker-compose up --build
~~~
- If container is already built:
~~~
$ docker-compose up
~~~
- If trying to wipe the local database:
~~~
$ docker-compose down --volumes
~~~

## How to use the Project
- To signup:
    - Navigate to localhost:8000/signup
    - Login with your new account details

- To login as a admin:
    - Username: admin
    - Password: admin


## Troubleshooting
- If docker-entrypoint.sh cannot be found when building and starting the container:
    - Navigate to ./app directory and find docker-entrypoint.sh, using an IDE such as VSC
    - At the bottom-right task bar, ensure end of line sequence is LF and save file with UTF-8 encoding
