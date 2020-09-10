## flask-userphone-api

Simple API for User-Phone numbers management using Python Flask (Flask-RESTPlus). The API built here will be used in a React front-end.

## Features and extensions

The following extensions will be used within the project:

```bash
Flask-restplus
Flask-Migrate
Flask-SQLAlchemy
Flask-Script
Namespaces(Blueprints)
Unittest
```

## Project structure

```bash
main/model - contains all database models
main/service - contains all the business logic of the application
main/controller - contains application endpoints
```
```bash
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── controller
│   │   │   └── user_controller.py
│   │   ├── model
│   │   │   └── user.py/phonenumber.py
│   │   └── service
│   │       └── user_service.py
│   └── test
│       └── base.py/test_config.py/test_phonebook.py
└── requirements.txt
```

##
After installing all the required packages, run the application using the command:
```bash
python manage.py run
```

or run the tests using the command:

```bash
python manage.py test
```
