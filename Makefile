migrate:
	- python typeyou/manage.py makemigrations typeyou
	- python typeyou/manage.py migrate


test:
	- pep8 .
	- python typeyou/manage.py test typeyou
