# Coding_Challenge
Simple REST API  for Users and Organizations implemented with Django Rest Framework
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following Software to run this project

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/releases/2.2.6/)
* [PIP 10.0.1 or greater](https://pypi.org/project/pip/)


* [VirtualEnv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) --not required but it is conventional to install all libraries in a virtualenv
'''
python3 -m pip install --user virtualenv
'''

### Installing

Install the project by running the following:

Clone the repo

```
 git clone https://github.com/danieldufek03/Coding_Challenge.git
```

```
cd Coding_Challenge/CodeChallenge/
```

startup virtualenv

```
virtualenv env
source env/Scripts/activate  
```

install django and django rest framework

```
pip install django
pip install djangorestframework
```
Run the application
```
python manage.py runserver
```

# How To

usage of this api, for this section we will assume the user is familiar with some
rest client such as postman or insomnia.

## View all Users

submitting a GET request to http://localhost:8000/users/ through postman or your web browser will display a list of all users and their attributes

## View all Organizations

submitting a GET request to http://localhost:8000/organizations/ through postman or your web browser will display a list of all organizations and their attributes

## View a single User

submit a GET request to http://localhost:8000/users/$user_id/ where $user_id is obtained from the id field of all users

## View a single Organization

submit a GET request to http://localhost:8000/organizations/$organization_id/ where $organization_id is obtained from the id field of all organizations

## Create a single User

Submit a POST request to http://localhost:8000/users/ with the following form data

Example...
```
username:Jimmy
password:Password123!@#
email:jimmy@gmail.com
first_name:Daniel
last_name:d
address:ddd
phone:444444
```

## Create a single Organization

Submit a POST request to http://localhost:8000/users/ with the following form data

Example...
```
name:Nextel
address:123 Nextel Way
phone:444444
```

## Add a user to an Organizations

Submit a POST request to http://localhost:8000/userorganizations/ with the following form data
you will need to use the id field from both organizations and users
Example...
```
users: 3
organizations: 2
```

## Delete a user from an Organizations

Submit a DELETE request with no form data to http://localhost:8000/userorganizations/$relationship_id/ which can be obtained by submitting a GET request to http://localhost:8000/userorganizations/


## Read all Users from an Organizations

by submitting a GET request to http://localhost:8000/organizations/$organization_id will return a field users which contains the user id's of all users in the organization

## Read all Organizations from a User

by submitting a GET request to http://localhost:8000/users/$user_id will return a field users which contains the organization id's of all organizations which the user belongs to




### Future Work
I would like to update in the future to have models be referenced by something more user friendly than the id field
