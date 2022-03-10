## 📎 Technologies

## Login API
- User: convidado
- Password: 123456

Project was developed with the following technologies:
- [Django-Rest-Framework](https://www.django-rest-framework.org/)

## 📎 Acquired knowledge
- I learned how to customize filters in searches
- How to correctly sort and search in a url

This is a project developed with the team **[Alura](https://www.alura.com.br/)**

<hr>

<p align="center">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#installing">Installing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#using-the-api">Using</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#routes">Routes</a>—↴
  <br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="#routes-to-clients">Clients</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <br>
 
<div align="center">
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://www.django-rest-framework.org/#requirements">
    <img alt="PyPI - Django Version" src="https://img.shields.io/pypi/djversions/djangorestframework?color=%2300C86F">
  </a>
  <a href="https://github.com/luigiMinardi/alurachallenge-backend/blob/main/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/badge/license-MIT-%2300C86F">
  </a>
  <a href="https://pypi.org/project/djangorestframework/">
    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/djangorestframework">
  </a>
</div>

## Installing

* First, clone the repository::

  ```bash
  git clone https://github.com/Gabriel-limadev/client-Api
  ```

* Then create a [Virtual Enviroment](https://outline.com/HaJ3zA) for you:

  ```bash
  python -m venv venv
  ```
  
* Activate Your `venv`:

  Mac/Linux:
  ```bash
  source .venv/bin/activate 
  ```
  Windows:
  ```cmd
  venv/Scripts/activate.bat
  ```

* Install all the requirements:

  ```bash
  pip install -r requirements.txt
  ```

* Make the Migrations:

  ```bash
  python manage.py makemigrations
  ```

* Run the DataBase Migration:

  ```bash
  python manage.py migrate
  ```

* Create a Super User:
  ```bash
  python manage.py createsuperuser
  ```

* Run your server:

  ```bash
  python manage.py runserver
  ```

Now you are ready to use it.

# Using the API

## Routes

### Routes to Clients

#### POST /clients/
###### The response code must be `201`.

Add a new client in the database.

##### Request Body:

```json
{
    "name": "Gabriel Lima",
    "email": "gabrielvitor180701@gmail.com",
    "cpf": "79416321010",
    "rg": "402208821",
    "smartphone": "11 98633-6634",
    "active": true
}
```

##### Response Body:

```json
{
    "id": 51,
    "name": "Gabriel Lima",
    "email": "gabrielvitor180701@gmail.com",
    "cpf": "79416321010",
    "rg": "402208821",
    "smartphone": "11 98633-6634",
    "active": true
}
```

#### PUT /clients/:id/
###### The response code must be `200`.

Change all values in specified client in the database.

##### Request Body:

> *Changing the client we've **POST** earlier, at url `/clients/51/`*
```json
{
    "id": 51,
    "name": "Gabriel Vitor Araujo de Lima",
    "email": "gabrielvitor@gmail.com",
    "cpf": "79416321010",
    "rg": "402208821",
    "smartphone": "11 98633-6634",
    "active": false
}
```

#### GET /clients/
###### The response code must be `200`.

Getting all the clients of the database.

##### Response Body:

```json
[
    {
        "id": 1,
        "name": "Alícia Pereira",
        "email": "alíciapereira@uol.com.br",
        "cpf": "23460162090",
        "rg": "283563567",
        "smartphone": "10 95641-8050",
        "active": false
    },
    {
        "id": 2,
        "name": "Alana da Rocha",
        "email": "alanadarocha@uol.com.br",
        "cpf": "29324981420",
        "rg": "833485686",
        "smartphone": "11 99538-4137",
        "active": true
    },
    {
        "id": 3,
        "name": "Emilly da Cruz",
        "email": "emillydacruz@gmail.com",
        "cpf": "82768441112",
        "rg": "285476140",
        "smartphone": "13 98428-4712",
        "active": false
    },

... 

        {
            "id": 51,
            "name": "Gabriel Vitor Araujo de Lima",
            "email": "gabrielvitor@gmail.com",
            "cpf": "79416321010",
            "rg": "402208821",
            "smartphone": "11 98633-6634",
            "active": false
        }
]
```

#### /clients/ Query Params

#### Search

You can search clients using the query param `search`.

##### Example 1:

> *Searching for client name Gabriel.*

Searching "Gabriel" doing `/clients/?search=Gabriel`

##### Return:

> *Returns all of the clients that match in the search.*
```json
[
    {
        "id": 15,
        "name": "Enzo Gabriel Oliveira",
        "email": "enzogabrieloliveira@hotmail.com",
        "cpf": "16441107252",
        "rg": "678546633",
        "smartphone": "12 97550-4115",
        "active": false
    },
    {
        "id": 23,
        "name": "Gabriel Ramos",
        "email": "gabrielramos@yahoo.com.br",
        "cpf": "96584818500",
        "rg": "672634992",
        "smartphone": "20 94564-9970",
        "active": false
    },
    {
        "id": 51,
        "name": "Gabriel Vitor Araujo de Lima",
        "email": "gabrielvitor@gmail.com",
        "cpf": "79416321010",
        "rg": "402208821",
        "smartphone": "11 98633-6634",
        "active": false
    }
]
```

##### Example 2:

> *Searching for client cpf 19915732511.*

Searching "19915732511" doing `/clients/?search=19915732511`

##### Return:

> *Returns all of the clients that match in the search.*
```json
[
    {
        "id": 4,
        "name": "Luiza Martins",
        "email": "luizamartins@gmail.com",
        "cpf": "19915732511",
        "rg": "166702052",
        "smartphone": "16 94447-7725",
        "active": true
    }
]
```
