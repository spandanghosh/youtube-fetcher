# app/routes.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Video
from datetime import datetime
import re

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    videos = Video.query.order_by(Video.published_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    
    return jsonify({
        'videos': [video.to_dict() for video in videos.items],
        'total': videos.total,
        'pages': videos.pages,
        'current_page': videos.page
    })

@api_blueprint.route('/videos/search', methods=['GET'])
def search_videos():
    query = request.args.get('q', '')
    if not query:
        return jsonify({'error': 'Search query is required'}), 400
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Create a regex pattern for partial matching
    words = query.split()
    pattern = '|'.join([re.escape(word) for word in words])
    
    # Search in title or description
    videos = Video.query.filter(
        db.or_(
            Video.title.op('REGEXP')(pattern),
            Video.description.op('REGEXP')(pattern)
        )
    ).order_by(Video.published_at.desc()).paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    
    return jsonify({
        'videos': [video.to_dict() for video in videos.items],
        'total': videos.total,
        'pages': videos.pages,
        'current_page': videos.page
    })