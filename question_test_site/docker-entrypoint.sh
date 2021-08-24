#!/bin/bash
echo "Collect static files"
python manage.py collectstatic --noinput

echo "Database migration"
python manage.py migrate

echo "Creating cache table"
python manage.py createcachetable

echo "Start celery worker"
celery -A question_test_site worker --loglevel=INFO

echo "Start celery beat"
celery -A question_test_site beat

echo "Start server"
python manage.py runserver localhost:8000