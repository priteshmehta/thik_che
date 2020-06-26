#!/bin/bash
gunicorn --workers 1 --bind 0.0.0.0:80 wsgi:app