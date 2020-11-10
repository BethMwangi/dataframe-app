import os

"""App configuration."""
from os import environ, path
from dotenv import load_dotenv


# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))





THEATRE_URL = environ.get('THEATRE_URL')
MOVIE_URL = environ.get('MOVIE_URL')

API_SECRET=environ.get('API_SECRET')
ZIP_CODE=environ.get('ZIP_CODE')
START_DATE=environ.get('START_DATE')
LINE_UP_ID=environ.get('LINE_UP_ID')
DATE_TIME=environ.get('DATE_TIME')

