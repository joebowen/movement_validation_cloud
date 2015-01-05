movement_validation_cloud
=========================

Movement validation cloud application

source content/djangodev/bin/activate

eb start

eb status --verbose

mysql -u root -p django
drop database django; create database django; use django; 
python manage.py syncdb
python manage.py runserver