# ==========================
# 🏗️ Stage 1: Build Stage
# ==========================
FROM python:3.10-slim AS builder

# Environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (minimize layers)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies (cache layers)
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files (cache layers)
COPY . /app/

# Collect static files (minimize layers)
RUN python manage.py collectstatic --noinput

# ==========================
# 🚀 Stage 2: Production Stage
# ==========================
FROM python:3.10-slim

# Environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy dependencies from the builder stage (minimize layers)
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code (minimize layers)
COPY --from=builder /app /app

# ✅ Ensure Waitress is installed (explicit check)
RUN pip show waitress || (echo "Waitress is missing in production!" && exit 1)

# Create a volume for media files (Fly.io volume mount)
# This is handled by Fly.io mounts in fly.toml, and the volume is not created here.
# You do not need this line: VOLUME /app/media

# Expose the correct port for Fly.io
EXPOSE 8080

# ✅ Start the application with Waitress
CMD ["python", "run_waitress.py"]