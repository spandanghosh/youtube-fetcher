## YouTube Video Fetcher

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey)
![Docker](https://img.shields.io/badge/docker-3.8+-blue)

A scalable backend service with admin dashboard that auto-fetches cricket videos from YouTube API (10s refresh, multi-key failover) and serves them via REST APIs with full-text search.

---

## ✨ Features

### Core Requirements
- ⏱ Continuous background fetching (every 10 seconds)
- 📄 Paginated API with chronological sorting
- 🗄 SQLite database storage with proper indexing
- 🐳 Dockerized deployment
- 🔍 Search API with partial matching

### Bonus Implementations
- 🔁 Multiple API key rotation
- 🔎 Optimized fuzzy search (e.g., "tea how" → "How to make tea?")
- 🛠 Basic admin dashboard

---

## 🚀 Quick Start

### Prerequisites
- [Docker Engine 20+](https://docs.docker.com/engine/install/)
- Python 3.9+ (for development without Docker)
- YouTube Data API keys (3 or more recommended to avoid quota limits)
## 📸 Screenshots

### Dashboard View
![Screenshot (1057)](https://github.com/user-attachments/assets/5d627a42-daea-464d-b3ad-78e37e4ed7d9)

*Video listing with search and pagination*

### API Response Example
```json
{
  "current_page": 2,
  "pages": 3,
  "total": 132,
  "videos": [
    {
      "channel_title": "Cricket with SR",
      "description": "",
      "id": "AljqptX1r5k",
      "published_at": "2025-04-10T16:31:25",
      "thumbnail_url": "https://i.ytimg.com/vi/AljqptX1r5k/default.jpg",
      "title": "over exata cover drive #cricket #indvsbanlivematchtoday #cricketmatch #ipl #crickethighlights"
    },
    {
      "channel_title": "short all vlogs",
      "description": "",
      "id": "qjGkWVZNHRw",
      "published_at": "2025-04-10T16:31:07",
      "thumbnail_url": "https://i.ytimg.com/vi/qjGkWVZNHRw/default.jpg",
      "title": "Bangalore vs Delhi #gameskhelkarpaisekai #cricket #cricketenthusiast #nationalteam #ipl #cricketlove"
    }
  ]
}
```
### WebURL View
![image](https://github.com/user-attachments/assets/c78d73f5-8941-4e23-a7c7-6f4f1af7fab1)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/spandanghosh/youtube-fetcher.git
   cd youtube-fetcher
2. **Configure environment**
```bash
cp .env
# Then open the `.env` file and add your YouTube API keys:
# YOUTUBE_API_KEYS=key1,key2,key3
```
3. **Start services using Docker**
```bash
docker-compose up --build
```
**📚 API Reference**
Base URL
```bash
http://localhost:5000/api
```
## API Endpoints

### `/api/videos`
- **Method:** `GET`  
- **Description:** Paginated video list (newest first)

### `/api/videos/search`
- **Method:** `GET`  
- **Description:** Fuzzy search by title/description

### `/api/dashboard`
- **Method:** `GET`  
- **Description:** Interactive dashboard (HTML)

## Query Parameters

- `page` *(optional)*  
  Page number for pagination.  
  **Default:** `1`

- `per_page` *(optional)*  
  Number of videos per page.  
  **Default:** `10`

- `q` *(optional, for `/search` endpoint)*  
  Search term used to filter videos by title.  
  **Example:** `q=dhoni highlights`

```bash
GET /api/videos/search?q=dhoni&page=2&per_page=5
```
## 🗂 Project Structure

```text
youtube-fetcher/
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── config.py               # Configuration loader
│   ├── models.py               # SQLAlchemy models
│   ├── routes.py               # API endpoints
│   ├── services/
│   │   ├── youtube_service.py  # YouTube API fetcher logic
│   │   └── background_tasks.py # Background fetch scheduler
│   └── utils/
│       └── helpers.py          # Utility functions
├── static/                     # Frontend static assets
├── templates/                  # Jinja2 templates
├── docker-compose.yml          # Docker service definitions
├── Dockerfile                  # Docker container configuration
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # Project documentation (this file)
```
## 🌐 Access Points

- **API Base URL:**  
  [http://localhost:5000/api](http://localhost:5000/api)

- **Dashboard (if enabled):**  
  [http://localhost:5000/dashboard](http://localhost:5000/dashboard)

## 📝 Development Notes

- **Data Flow:**  
  YouTube API → Flask Backend → SQLite Database → API Consumers

- **API Key Rotation:**  
  Automatically rotates between available API keys if quota is exhausted.

- **Search Mechanism:**  
  Uses regex-based partial and fuzzy matching — designed to handle out-of-order, loosely typed queries.

## 📜 License 
This project is developed as part of the FamPay Backend Assignment. All rights reserved by the assignment terms.

Key improvements made: (📅 Last Updated: 2025-04-11)
1. **Simplified Setup**: Combined Docker/Manual instructions
2. **Added Troubleshooting**: Common issues section
3. **Clearer API Docs**: Table format with curl examples
4. **Visual Enhancements**: More badges and spacing
5. **Key Rotation Highlight**: Emphasized in Features
6. **Timestamp**: Added last updated date

## 📌 API Reference
- [YouTube Data API v3 Docs](https://developers.google.com/youtube/v3)
- [Search API Reference](https://developers.google.com/youtube/v3/docs/search/list)


