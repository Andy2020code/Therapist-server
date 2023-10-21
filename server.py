from bottle import Bottle, run, static_file
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Bottle()

@app.route('/')
def index():
    return 'Hello, World! This is a Bottle WSGI application.'

@app.route('/html/<filename>')
def serve_html(filename):
    return static_file(filename, root='./html/')

# Add a route to serve your CSS file
@app.route('/css/<filename>')
def serve_css(filename):
    return static_file(filename, root='./css/')

@app.route('/IMG/<filename>')
def serve_images(filename):
    return static_file(filename, root='./IMG/')

@app.route('/js/<filename>')
def serve_js(filename):
    return static_file(filename, root='./js/')

# Add routes for specific HTML pages
@app.route('/index')
def serve_index():
    return static_file('index.html', root='./html/')

@app.route('/our-services')
def serve_our_services():
    return static_file('our-services.html', root='./html/')

@app.route('/therapists')
def serve_therapists():
    return static_file('therapists.html', root='./html/')

@app.route('/take-action')
def serve_take_action():
    return static_file('take-action.html', root='./html/')

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
        run(app, host='0.0.0.0', port=8000)

    # Create a watchdog event handler
    class FileChangeHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            on_change(event)

    # Set up the observer to watch for file system changes
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    run(app, host='localhost', port=5000)
