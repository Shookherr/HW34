#!/usr/bin/bash
python manage.py collectstatic -c --no-input
status=$?
exec "$@"