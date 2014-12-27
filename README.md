movement_validation_cloud
=========================

Movement validation cloud application

$ . content/djangodev/bin/activate

eb start

eb status --verbose

echo "drop database django; create database django; use django;" | mysql -u root -p django
python manage.py syncdb
python manage.py runserver