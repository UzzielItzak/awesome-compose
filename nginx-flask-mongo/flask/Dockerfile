# syntax=docker/dockerfile:1.4
FROM python:3.9-slim-buster AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port the Flask app listens on
EXPOSE 9090

# Run the Flask app
CMD ["python3", "server.py"]