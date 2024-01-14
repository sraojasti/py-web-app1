#!/bin/sh

# Api service is dependent on the db services up and healthy


echo "Waiting for postgres ....."
while ! nc - api-db 5432
do
    sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0

