# Youtube Video Fetcher
!{Python](https://img.shields.io/badge/python-3.9+-blue)
[200~# YouTube Video Fetcher

![Python](https://img.shields.io/badge/python-3.9+-blue)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey)
![Docker](https://img.shields.io/badge/docker-compose-3.8+-blueviolet)

A backend service that fetches cricket videos from YouTube API and provides searchable REST endpoints.

## ✨ Features

### Core Requirements
- Continuous background fetching (10s interval)
- Paginated API with chronological sorting
- Database storage (SQLite) with proper indexing
- Dockerized deployment
- Search API with partial matching

### Bonus Implementations
- Multiple API key rotation
- Optimized search (supports partial matches like "tea how" → "How to make tea?")
- Basic admin dashboard

## 🚀 Quick Start

### Prerequisites
- Docker Engine 20+
- Python 3.9+
- YouTube API keys (3 recommended)

### Setup
1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/youtube-fetcher.git
   cd youtube-fetcher
