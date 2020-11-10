import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, date, timedelta
from structlog import get_logger


import requests
import json

import pandas as pd
from pandas import json_normalize 

from sqlalchemy import create_engine 

from config import  *

cnx = create_engine('sqlite:///database.db').connect() 

logger = get_logger()



# API_SECRET="jjheffh3hkwz5df3d4ymcw4q"
# ZIP_CODE="60611"
# LINE_UP_ID="USA-TX42500-X"

current_date = date.today().isoformat()
my_date = datetime.now()


today_date = my_date.strftime("%Y-%m-%dT%H:%M:%SZ")



# def parse_date(DATE_TIME):
#     print(datetime.strptime(DATE_TIME, '%Y-%m-%dT%H:%M:%S.%f%z'))
#     return datetime.strptime(DATE_TIME, '%Y-%m-%dT%H:%M:%S.%f%z')


def get_api_data(line_up_id, start_date, zip, startDateTime, api_key):
    data = {
        'lineupId':LINE_UP_ID,
        'startDateTime':current_date,
        'start_date':today_date,
        'zip':ZIP_CODE,
        'api_key':API_SECRET,

    }

    url = "http://data.tmsapi.com/v1.1/movies/airings"
    
        
    response = requests.get(url=url, params=data)
    data_resp = {}
    logger.log('get-api-movies', resp=response.json(), status=response.status_code)
    if response.status_code == 200:
        data_resp = response.json()

    return data_resp



def list_movie_count():
    df_movie = pd.read_sql_table('movie_channel', cnx) 
    df_channel = pd.read_sql_table('movie_theatre', cnx) 

    merge_genres = pd.merge(df_movie, df_channel, on='genres')
    # list the top 5 genres count
    n = 5
    p = merge_genres['genres'].value_counts()[:n]
    print(p)

   


if __name__ == '__main__':
    get_api_data("USA-TX42500-X","2020-11-10", "60611", "2020-11-10T19%3A00Z","taxhm87ravg9behksfgsjba5")
    list_movie_count()
