#!/bin/bash
echo "Create migrations"
python manage.py makemigrations inseapp
echo "================================"

echo "Migrate"
python manage.py migrate
echo "================================"

echo "Start Server"
python manage.py runserver 0.0.0.0:8000