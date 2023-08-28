# create virtual environment 

> python -m venv c:\Django 

# activation under bin folder

> Cd\django>bin\activate 

# install django

C:\Django> pip3 install django

# create project 

> C:\djenv>django-admin startproject demoproject .

# start app

>python manage.py startapp <name of app>


# makemigrations - generating a database table

> python manage.py makemigrations

# migrate - synchronizes the database state with the currently declared models and migrations

> python manage.py migrate

# open python shell inside project 

>python manage.py shell

# run server

> python manage.py runserver