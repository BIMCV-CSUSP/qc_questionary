#!/bin/bash

source venv/bin/activate
gunicorn -b localhost:8000 -w 4 app:app 
#flask run
