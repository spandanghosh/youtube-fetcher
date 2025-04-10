# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        from app.routes import api_blueprint
        app.register_blueprint(api_blueprint)

        db.create_all()

        # Start background scheduler
        from app.services.background_tasks import fetch_latest_videos
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            func=fetch_latest_videos,
            trigger="interval",
            seconds=10,
            args=[app]
        )
        scheduler.start()

    return app