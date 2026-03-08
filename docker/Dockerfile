FROM python:3.11-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Expose ports for both API and UI
EXPOSE 8000
EXPOSE 8080

# Create a non-root user
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Default command (can be overridden, defaults to running API)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
