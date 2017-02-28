#!/bin/bash
# Start Gunicorn processes
echo Starting Gunicorn.
#cd validation
exec gunicorn validation.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
