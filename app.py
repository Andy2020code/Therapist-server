from flask import Flask, render_template
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is a Flask application.'

# Add a route to serve your CSS file
@app.route('/css/<filename>')
def serve_css(filename):
    return app.send_static_file('css/' + filename)

# Add a route to serve your image files
@app.route('/IMG/<filename>')
def serve_images(filename):
    return app.send_static_file('IMG/' + filename)

# Add a route to serve your JavaScript files
@app.route('/js/<filename>')
def serve_js(filename):
    return app.send_static_file('js/' + filename)

# Add routes for specific HTML pages
@app.route('/index')
def serve_index():
    return render_template('index.html')

@app.route('/our-services')
def serve_our_services():
    return render_template('our-services.html')

@app.route('/therapists')
def serve_therapists():
    return render_template('therapists.html')

@app.route('/take-action')
def serve_take_action():
    return render_template('take-action.html')

if __name__ == '__main__':
    if sys.platform == 'win32':
        # Windows-specific code
        import msvcrt
        # Perform Windows-specific file operations using msvcrt

    # Function to handle changes and restart the server
    def on_change(event):
        print("Change detected. Restarting the server.")
        observer.stop()
        observer.join()
        app.run(host='0.0.0.0', port=8000, threaded=True)

    # Create a watchdog event handler
    class FileChangeHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            on_change(event)

    # Set up the observer to watch for file system changes
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    # Use Gunicorn to run the Flask app
    from gunicorn import util

    if not util.is_dropprivileges_supported():
        app.run(host='0.0.0.0', port=80, threaded=True)
    else:
        print("Please run Gunicorn separately as shown in the instructions.")
