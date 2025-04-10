# app/models.py
from app import db
from datetime import datetime

class Video(db.Model):
    id = db.Column(db.String(50), primary_key=True)  # YouTube video ID
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    published_at = db.Column(db.DateTime, nullable=False, index=True)
    thumbnail_url = db.Column(db.String(255))
    channel_title = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'published_at': self.published_at.isoformat(),
            'thumbnail_url': self.thumbnail_url,
            'channel_title': self.channel_title
        }