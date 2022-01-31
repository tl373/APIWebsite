#!/bin/sh
export FLASK_APP=run
export FLASK_ENV=development
source $(pipenv --venv)/bin/activate
flask run -p 3000