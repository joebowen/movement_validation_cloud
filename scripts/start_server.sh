#!/bin/bash

python ../manage.py test --noinput
nohup python ../manage.py runserver &