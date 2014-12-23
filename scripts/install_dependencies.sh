#!/bin/bash

pip install  -r '../requirements.txt'
python ../manage.py createsuperuser --username django --noinput
