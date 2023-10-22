from flask import Flask, render_template

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5000)
