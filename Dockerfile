# Stage 1: Builder stage for Python dependencies
FROM python:3.9-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.9-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application files
COPY . .

# Set up static files directory
RUN mkdir -p /app/app/static && \
    chown -R nobody:nogroup /app && \
    chmod -R 755 /app/app/static

# Environment variables with defaults
ENV GUNICORN_WORKERS=4 \
    GUNICORN_THREADS=2 \
    GUNICORN_BIND="0.0.0.0:5000" \
    GUNICORN_ACCESS_LOGFILE="-"

# Switch to non-root user
USER nobody

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/api/videos || exit 1

# Run command
CMD ["sh", "-c", "gunicorn --workers ${GUNICORN_WORKERS} --threads ${GUNICORN_THREADS} --bind ${GUNICORN_BIND} --access-logfile ${GUNICORN_ACCESS_LOGFILE} 'app:create_app()'"]