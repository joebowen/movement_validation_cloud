movement_validation_cloud
=========================

Movement Validation cloud application

The cloud application for the [movement_validation python package](https://github.com/openworm/movement_validation)

source content/djangodev/bin/activate

eb start

eb status --verbose

mysql -u root -p django
drop database django; create database django; use django; 
python manage.py syncdb
python manage.py runserver
