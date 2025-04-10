# app/config.py
import os
from datetime import datetime, timedelta

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///videos.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    YOUTUBE_API_KEYS = os.getenv('YOUTUBE_API_KEYS', '').split(',')
    YOUTUBE_SEARCH_QUERY = os.getenv('YOUTUBE_SEARCH_QUERY', 'cricket')
    FETCH_INTERVAL_SECONDS = int(os.getenv('FETCH_INTERVAL_SECONDS', '10'))
    MAX_RESULTS_PER_REQUEST = int(os.getenv('MAX_RESULTS_PER_REQUEST', '50'))