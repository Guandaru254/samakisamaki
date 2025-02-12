from waitress import serve
from samakisamaki.wsgi import application  # Import your WSGI application

if __name__ == "__main__":
    print("Starting Waitress server on port 8000...")
    serve(application, host="0.0.0.0", port=8000)
    