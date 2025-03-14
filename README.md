# SPAC - Cereal API - Week 3
A REST API serving information on cereals - an exercise in CRUD, API auth and database management.

This project is developed using 
[Python](https://www.python.org/), 
[Django](https://www.djangoproject.com/), 
[Django REST Framework](https://www.django-rest-framework.org/),
[Docker](https://docs.docker.com/) and [Postgresql](https://www.postgresql.org/)

## Features
 - Web API serving company product data
 - Renders data in application/json as well as a text/html web view
 - Allows the viewing of product data even for unauthenticated users
 - Creating, updating and deleting data is reserved for authenticated users. Authentication is session based and requires login of registered user.
 - Provides filtering options for all product fields

## Requirements
 - [Docker](https://docs.docker.com/engine/install/)
 - [Python::3.12](https://www.python.org/downloads/release/python-3120/)

## Installation

First ensure that docker-daemon is running

The database is containerized with Docker for ease of use in development.
In the project a docker-compose.yml schema is provided. To initialize the database simply run the following command from a terminal in the project root:
```sh
docker compose up -d
```

Once the database is up and running you can now start initializing the django project.
Firstly, create a new python virtual environment:
```sh
python3 -m venv .venv
```
and start the environment
```sh
- Unix/macos
source .venv/bin/activate

- Windows (PowerShell)
.venv\Scripts\activate.ps1

- Windows (cmd.exe)
.venv\Scripts\activate.bat
```

Next up, install the necessary requirements:
```sh
pip install -r requirements.txt
```

## Get Started
The following steps are required in order to get the application up and running:

1. Start by migrating changes to the database:
    ```sh
    python manage.py migrate
    ```

2. Create a superuser to use for API authentication:
    ```sh
    python manage.py createsuperuser
    ```

3. Populate lookup tables in the database with categorical data from Cereal.csv:
    ```sh
    python manage.py provision
    ```

4. Populate the database with product data from the Cereal.csv file:
    ```sh
    python manage.py seed
    ```

Once the above steps have been completed you are now ready to start the application:

```sh
python manage.py runserver
```

With the server up an running, you can use the API on: [localhost:8000](http://127.0.0.1:8000/)

## API Reference

### Authentication
|  Path            | Method(s)  | Usage                                                   |
| ---------------- | ---------- | ------------------------------------------------------- |
| /api-authlogin/  | GET        | Web view of login page                                  |
| /api-authlogin/  | POST       | Authenticating to the server with username and password |
| /api-authlogout/ | POST       | Authenticating to the server                            |

### Products

|  Path           | Method(s)  | Usage                  | Authentication required? |
| --------------- | ---------- | -----------------------| ------------------------ |
| /products/      | GET        | Viewing all products   | ❌                      |
| /products/      | POST       | Creating a new product | ✅                      |
| /products/{id}/ | GET        | Viewing a product      | ❌                      |
| /products/{id}/ | PUT, PATCH | Updating a product     | ✅                      |
| /products/{id}/ | DELETE     | Deleting a product     | ✅                      |


### Manufacturers

|  Path                | Method(s)  | Usage                        | Authentication required? |
| -------------------- | ---------- | ---------------------------- | ------------------------ |
| /manufacturers/      | GET        | Viewing all manufacturers    | ❌                      |
| /manufacturers/      | POST       | Creating a new manufacturers | ✅                      |
| /manufacturers/{id}/ | GET        | Viewing a manufacturer       | ❌                      |
| /manufacturers/{id}/ | PUT, PATCH | Updating a manufacturer      | ✅                      |
| /manufacturers/{id}/ | DELETE     | Deleting a manufacturer      | ✅                      |

### Thermal Types
|  Path               | Method(s)  | Usage                      | Authentication required? |
| ------------------- | ---------- | -------------------------- | ------------------------ |
| /thermaltypes/      | GET        | Viewing all thermaltypes   | ❌                      |
| /thermaltypes/      | POST       | Creating a new thermaltype | ✅                      |
| /thermaltypes/{id}/ | GET        | Viewing a thermaltype      | ❌                      |
| /thermaltypes/{id}/ | PUT, PATCH | Updating a thermaltype     | ✅                      |
| /thermaltypes/{id}/ | DELETE     | Deleting a thermaltype     | ✅                      |