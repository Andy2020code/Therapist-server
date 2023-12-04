from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'serverform45@gmail.com'
app.config['MAIL_PASSWORD'] = 'Anderson@2020'
app.config['MAIL_DEFAULT_SENDER'] = 'serverform45@gmail.com'

mail = Mail(app)

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

@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    data = request.json  # Get JSON data from the request

    # Process the form data as needed
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Perform any necessary validation or email sending logic here

    # Send email
    try:
        send_email(name, email, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

    return 'OK', 200  # Return a simple response to the client

def send_email(name, email, message):
    recipient_email = 'andersonromanodasilva2020@gmail.com'  # Replace with the recipient's email address

    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    msg = Message(subject, recipients=[recipient_email])
    msg.body = body

    try:
        mail.send(msg)
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
