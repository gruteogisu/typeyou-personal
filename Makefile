migrate:
	- python typeyou/manage.py makemigrations typeyou users community
	- python typeyou/manage.py migrate


test:
	- pep8 .
	- python typeyou/manage.py test typeyou users community
