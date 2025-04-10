#!/bin/sh
exec gunicorn \
    --workers ${GUNICORN_WORKERS:-4} \
    --threads ${GUNICORN_THREADS:-2} \
    --bind ${GUNICORN_BIND:-0.0.0.0:5000} \
    "app:create_app()"
