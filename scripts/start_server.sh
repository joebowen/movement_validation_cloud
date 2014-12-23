#!/bin/bash

export SUPER_USER=django
export SUPER_USER_PASSWORD=change
python manage.py create_superuser
nohup python ../manage.py runserver &