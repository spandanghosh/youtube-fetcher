# app/services/youtube_service.py
import os
import requests
from datetime import datetime, timedelta
from app import db
from app.models import Video

class YouTubeService:
    BASE_URL = "https://www.googleapis.com/youtube/v3/search"
    
    def __init__(self, api_keys):
        self.api_keys = api_keys
        self.current_key_index = 0
    
    def get_current_key(self):
        return self.api_keys[self.current_key_index]
    
    def rotate_key(self):
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
    
    def fetch_videos(self, query, max_results=50):
        published_after = (datetime.utcnow() - timedelta(minutes=5)).isoformat() + "Z"
        params = {
            'part': 'snippet',
            'q': query,
            'type': 'video',
            'order': 'date',
            'maxResults': max_results,
            'publishedAfter': published_after,
            'key': self.get_current_key()
        }
        
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json().get('items', [])
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:  # Quota exceeded
                self.rotate_key()
                return self.fetch_videos(query, max_results)
            raise
        except Exception as e:
            print(f"Error fetching videos: {e}")
            return []
    
    def store_videos(self, videos_data):
        new_videos = 0
        for item in videos_data:
            video_id = item['id']['videoId']
            if Video.query.get(video_id):
                continue
                
            snippet = item['snippet']
            video = Video(
                id=video_id,
                title=snippet['title'],
                description=snippet['description'],
                published_at=datetime.strptime(snippet['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                thumbnail_url=snippet['thumbnails']['default']['url'],
                channel_title=snippet['channelTitle']
            )
            db.session.add(video)
            new_videos += 1
        
        db.session.commit()
        return new_videos