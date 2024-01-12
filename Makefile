ROOT_DIR:=./
VENV_BIN_DIR:=".venv/bin"

VIRTUALENV:=$(shell which virtualenv)

REQUIREMENTS_DIR:="requirements"
REQUIREMENTS_LOCAL:="$(REQUIREMENTS_DIR)/requirements.txt"

PIP:="$(VENV_BIN_DIR)/pip"
CMD_FROM_VENV:=". $(VENV_BIN_DIR)/activate; which"
PYTHON=$(shell "$(CMD_FROM_VENV)" "python")

DJANGO_SUPERUSER_USERNAME="admin"
DJANGO_SUPERUSER_EMAIL="admin@admin.com"
DJANGO_SUPERUSER_PASSWORD="admin@123"


define create-venv
	python3 -m venv .venv
endef

venv:
	@$(create-venv)
	@$(PIP) install --upgrade pip
	@$(PIP) install -r $(REQUIREMENTS_LOCAL)

clean:
	@rm -rf .cache
	@rm -rf .venv
	@find . -name *.pyc -delete
	@find . -type d -name __pycache__ -delete
	@rm -rf htmlcov coverage.xml .coverage
	@rm -rf .idea
	@rm -rf celerybeat-schedule.db

collectstatic: venv
	@$(PYTHON) ./manage.py collectstatic --no-input

migrate: venv
	@$(PYTHON) ./manage.py migrate

superuser: venv
	@DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) $(PYTHON) ./manage.py createsuperuser --username $(DJANGO_SUPERUSER_USERNAME) --email $(DJANGO_SUPERUSER_EMAIL) --no-input
	@echo "Superuser created with follwing credentials:"
	@echo "Username: "$(DJANGO_SUPERUSER_USERNAME)
	@echo "Email: "$(DJANGO_SUPERUSER_EMAIL)
	@echo "Password: "$(DJANGO_SUPERUSER_PASSWORD)
	@echo "Use this credentials to login at http://127.0.0.1:8000/admin/"

run-local: venv
	@echo "\n"
	@echo "----------------------------------------------------------------------------------------------------------------------------------------"
	@echo "| !! Hurray, setup completed, for development purpose you can activate your vitual environment by running 'source .venv/bin/activate'. |"
	@echo "----------------------------------------------------------------------------------------------------------------------------------------"
	@echo "\n"
	@$(PYTHON) ./manage.py runserver

docker:
	@docker-compose -f docker-compose-local.yml up --build

docker-shell:
	@docker-compose -f docker-compose-local.yml run application python manage.py shell_plus

docker-superuser:
	@docker-compose -f docker-compose-local.yml run application python manage.py createsuperuser --no-input
	@echo "Superuser created with follwing credentials:"
	@echo "Username: "$(DJANGO_SUPERUSER_USERNAME)
	@echo "Email: "$(DJANGO_SUPERUSER_EMAIL)
	@echo "Password: "$(DJANGO_SUPERUSER_PASSWORD)
	@echo "Use this credentials to login at http://127.0.0.1:8000/admin/"

start: venv collectstatic migrate run-local
