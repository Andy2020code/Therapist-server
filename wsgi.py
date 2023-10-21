from app import app  # Import your Flask app
import sys

if __name__ == "__main__":
    if sys.platform == "win32":
        import msvcrt
        # Perform Windows-specific file operations using msvcrt

    # Start the Flask app using Gunicorn
    app.run(host="0.0.0.0", port=8080, threaded=True)
