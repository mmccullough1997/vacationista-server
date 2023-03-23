#!/bin/bash

# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands

heroku pg:reset --app vacationista --confirm vacationista
heroku run python3 manage.py migrate --app vacationista
heroku run python3 manage.py makemigrations vacationistaapi --app vacationista
heroku run python3 manage.py migrate vacationistaapi --app vacationista
heroku run python3 manage.py loaddata users articles recommendations highlights event_types expense_types transportation_types legs trips events expenses transportations trip_legs --app vacationista
