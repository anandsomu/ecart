#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

export ENV_TYPE=local

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py runserver 0.0.0.0:8000