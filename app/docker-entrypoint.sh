#!/bin/sh

# Apply database migrations
echo "###   Applying database migrations   ###"
python manage.py makemigrations
python manage.py migrate

# Refresh static files
python manage.py collectstatic --noinput

# Start server
echo "###   Starting server   ###"
python manage.py runserver 0.0.0.0:8000 & python telebot.py runserver 0.0.0.0:8001

