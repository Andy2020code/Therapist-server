from flask import Flask, render_template
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread
from waitress import serve  # Import Waitress

app = Flask(__name__)

@app.route('/')
def index():
    # Perform the redirection to your Route 53 domain
    return redirect("http://arv2.net")

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
        serve_thread = Thread(target=serve_app)
        serve_thread.start()

    def serve_app():
        serve(app, host='http://arv2.net', port=5000)  # Use Waitress to serve the app

    # Create a watchdog event handler
    class FileChangeHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            on_change(event)

    # Set up the observer to watch for file system changes
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    serve_thread = Thread(target=serve_app)
    serve_thread.start()
