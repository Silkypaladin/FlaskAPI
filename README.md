
# Quizly API

Quizly is an API written in Flask, made as a practice of a general API mechanisms and concept.  It is also supposed to serve as a simple backend for a Quiz website (still in development process).

## Installation

Packages required to properly run the project are listed in **requirements.txt** file. To install them run:

```bash
pip install -r requirements.txt
```
or (for Python3 users):
```bash
pip3 install -r requirements.txt
```

## Project structure
The project consists of: **app.py**, serving as a main function, **data.db** (both of those located in the main project directory) and **/api** directory, containing all of the logic. Under **api/** you will find  constants, model and config files, **routes/** directory, containg all the endpoints and **extensions/** with helper and database management files. **__init__.py** is a file containing application factory method.
```
    .
    ├── api 
    │   ├── routes
    │   │   ├── login.py
    │   │   ├── question.py
	│	│   ├── quiz.py
	│	│   ├── user.py
	│	├── extensions
    │   │   ├── database.py
    │   │   ├── helpers.py
    │   ├── __init__.py
    │   ├── config.py
    │   ├── models.py
    │   ├── app.db
    │   ├── test_app.db
    │
    ├── tests.py
    ├── README.md
    └── app.py  

```

## Usage
To start the API run (when in main project folder):
```python
python app.py
```
The API runs under http://127.0.0.1:5000/api address. You need to log in using basic auth to get JWT token and send it in **x-access-token** header. To run the tests simply type:
```python
python tests.py
```
