# app/services/background_tasks.py
from datetime import datetime, timedelta
from app import db
from app.models import Video
from app.services.youtube_service import YouTubeService
from app.config import Config

def fetch_latest_videos(app):
    with app.app_context():
        youtube = YouTubeService(Config.YOUTUBE_API_KEYS)
        print(f"{datetime.utcnow()} - Fetching latest videos...")
        
        videos_data = youtube.fetch_videos(
            Config.YOUTUBE_SEARCH_QUERY,
            Config.MAX_RESULTS_PER_REQUEST
        )
        
        new_videos = youtube.store_videos(videos_data)
        print(f"Added {new_videos} new videos to the database.")