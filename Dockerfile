# Stage 1: Build stage
FROM python:3.10-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install required system packages and clean up
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev curl && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Stage 2: Production stage
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the application from the builder stage
COPY --from=builder /app /app

# Reinstall Python dependencies to avoid compatibility issues
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Verify that Waitress is installed in the production stage
RUN pip show waitress || (echo "Waitress is missing in the production stage!" && exit 1)

# Create a volume for media files
VOLUME /app/media

# Fly.io expects your app to listen on port 8080
EXPOSE 8080

# Start the application with Waitress
CMD ["python", "run_waitress.py"]
