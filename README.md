#movement_validation_cloud#

The Movement Validation cloud application, for the [movement_validation Python package](https://github.com/openworm/movement_validation).

For installation instructions, please see [INSTALL.md](https://github.com/joebowen/movement_validation_cloud/blob/master/INSTALL.md).

**@JoeBowen's Notes**

source content/djangodev/bin/activate

eb start

eb status --verbose

mysql -u root -p django
drop database django; create database django; use django; 
python manage.py syncdb
python manage.py runserver
