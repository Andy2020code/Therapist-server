from flask import Flask, render_template
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Thread
import gunicorn.app.base
from gunicorn.six import iteritems

app = Flask(__name)

@app.route('/')
def index():
    return render_template('index.html')

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
    # Function to handle changes and restart the server
    def on_change(event):
        print("Change detected. Restarting the server.")
        observer.stop()
        observer.join()
        serve_thread = Thread(target=serve_app)
        serve_thread.start()

    def serve_app():
        # Use Gunicorn to serve the app
        options = {
            'bind': '0.0.0.0:5000',
            'workers': 4  # You can adjust the number of workers as needed
        }

        class StandaloneApplication(gunicorn.app.base.BaseApplication):
            def __init__(self, app, options=None):
                self.application = app
                self.options = options or {}
                super(StandaloneApplication, self).__init__()

            def load_config(self):
                config = {
                    key: value for key, value in iteritems(self.options)
                    if key in self.cfg.settings and value is not None
                }
                for key, value in iteritems(config):
                    self.cfg.set(key, value)

            def load(self):
                return self.application

        StandaloneApplication(app, options).run()

    # Create a watchdog event handler
    class FileChangeHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            on_change(event)

    # Set up the observer to watch for file system changes
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()

    # Use Gunicorn to serve the app
    serve_thread = Thread(target=serve_app)
    serve_thread.start()
