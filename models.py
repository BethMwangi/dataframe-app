import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class TheatreMovie(Base):
    """Table that stores the movies played in theatres"""
    __tablename__ = 'movie_theatre'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=False)
    release_year = Column(String(255), unique=False)
    genres = Column(String(255), unique=False)
    description = Column(String(255), unique=False)
    theatre = Column(String(255), unique=False)

    def __str__ (self):
    	return '{} - {} - {} - {}'.format(self.title, self.release_year, self.genres, self.theatre)



class ChannelMovie(Base):
    """Table that stores the movies played in channels"""
    __tablename__ = 'movie_channel'

    id = Column(Integer, primary_key=True)
    release_year = Column(String(255), unique=False)
    genres = Column(String(255), unique=False)
    description = Column(String(255), unique=False)
    channel = Column(String(255), unique=False)

    def __str__ (self):
    	return '{} - {} - {}'.format(self.release_year, self.genres, self.channel)





engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)