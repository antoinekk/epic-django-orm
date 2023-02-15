### General Info
***
CRM developed with Django Rest Framework.

### Installation and run
***
Please follow the instructions below to use and run the application :

Install PostgreSQL

```
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

Create your database

```
sudo -u postgres psql
```
```
CREATE DATABASE yourdb;
CREATE USER youradmin WITH ENCRYPTED PASSWORD 'yourpassword';
ALTER ROLE youradmin SET client_encoding TO 'utf8';
GRANT ALL PRIVILEGES ON DATABASE yourdb TO youradmin;
```

Clone the repository

```
git clone https://github.com/antoinekk/epic-django-orm.git <your path>
```

Create and activate the virtual environment

```
cd epic-django-orm
python3 -m venv env
source env/bin/activate
```

Change database settings in settings.py file

```
'NAME': 'yourdb',
'USER': 'youradmin',
'PASSWORD': 'yourpassword'
```

Install python modules provided in the "requirements.txt"

```
pip install -r requirements.txt
```

Run Django server

```
python manage.py runserver
```

Access

```
Create a management team user by using the API: POST http://localhost:8000/api/login/

Body example :

{
    "email" : "admin@admin.com",
    "password" : "admin",
    "team" : "MANAGEMENT"
}

Then you can access to the admin console : http://localhost:8000/admin

Or you can use the API to create new users, clients, contracts and events
```
