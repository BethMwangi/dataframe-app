import os
import sys

import csv, sqlite3
import json
import pandas as pd
from pandas import json_normalize
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


from urllib.request import urlopen

import  requests
import config

from config import  THEATRE_URL, MOVIE_URL

# Base = declarative_base() 

print(THEATRE_URL)
print(MOVIE_URL)
response = requests.get(MOVIE_URL)
print(response.status_code)

data = response.json()


df = pd.json_normalize(data)

df.to_csv("movie.csv", index=False, sep=',', encoding="utf-8")


sql_engine = create_engine('sqlite:///database.db')
conn = sql_engine.connect()
conn.execute("CREATE TABLE movie_theatre (release_year, genres, description, theatre);")

with open('output.csv', 'rt') as f:
    data = csv.reader(f)
    to_db =  [(i[4], i[9], i[11], i[18]) for i in data]
    
cur.execute("INSERT INTO movie_theatre (release_year, genres, description, theatre) VALUES (?, ?, ?, ?);", to_db)

conn.commit()
conn.close()
  












        