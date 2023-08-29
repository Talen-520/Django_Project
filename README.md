# Django_Project

### Demo havent uplodade yet , working on it...
model form:

http://127.0.0.1:8000/home

url pattern:

http://127.0.0.1:8000/dishes/<str:dish>

items = {
        'pasta':'pasta with red sauce',
        'falafel':'falafel with hummus',
        'cheesecake':'cheesecake with cherry topping',
    }

query URL:

http://127.0.0.1:8000/getuser/?

http://127.0.0.1:8000/getuser/?name=John&id=1

Attributes 

http://127.0.0.1:8000/attributes

date:

http://127.0.0.1:8000/display_date

serverStatus:

http://127.0.0.1:8000/ServerStatus









# hands on guidance 

# create virtual environment 

> python -m venv c:\Django 

#activation under bin folder

> Cd\django>bin\activate 

# install django

C:\Django> pip3 install django

#create project 

> C:\djenv>django-admin startproject demoproject .

#start app

>python manage.py startapp <name of app>


# makemigrations - generating a database table

> python manage.py makemigrations

# migrate - synchronizes the database state with the currently declared models and migrations

> python manage.py migrate

# open python shell inside project 

>python manage.py shell

# run server

> python manage.py runserver
