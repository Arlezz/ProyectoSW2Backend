#!/bin/bash

DJANGO_SUPERUSER_PASSWORD=test 

{
    # espero a que prmero se levante la base de datos antes de ejecutar las migraciones e iniciar el servidor
    python manage.py makemigrations; 
    python manage.py migrate;
    python manage.py runserver;
    python manage.py createsuperuser --username root --email root@mail.com --noinput
    #python manage.py collectstatic --no-input
    #gunicorn espacio_industrial.wsgi:application --bind 0.0.0.0:8000;
}