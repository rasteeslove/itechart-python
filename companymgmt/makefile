all:
	echo "default action not specified"

launch_local_dev:
	export CMGMT_DATABASE_MODE=local_dev; \
	python manage.py makemigrations; \
	python manage.py migrate; \
	python manage.py runserver

launch_local_tests:
	export CMGMT_DATABASE_MODE=local_test; \
	python manage.py makemigrations; \
	python manage.py migrate; \
	python manage.py runserver

run_local_tests:
	export CMGMT_DATABASE_MODE=local_test; \
	python manage.py makemigrations; \
	python manage.py migrate; \
	coverage run -m pytest -rP

launch_dev_docker:
	export CMGMT_DATABASE_MODE=docker_dev; \
	docker-compose -f docker-compose-dev.yml build; \
	docker-compose -f docker-compose-dev.yml up

run_docker_tests:
	export CMGMT_DATABASE_MODE=docker_test; \
	docker-compose -f docker-compose-test.yml build; \
	docker-compose -f docker-compose-test.yml up
