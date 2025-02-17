from waitress import serve
from samakisamaki.wsgi import application  # Import your WSGI application
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Default to Fly.io's expected port 8080
    print(f"Starting Waitress server on port {port}...")
    serve(application, host="0.0.0.0", port=port)
