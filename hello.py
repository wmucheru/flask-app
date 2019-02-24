import os, uuid

from flask import Flask, url_for, request, render_template, send_from_directory
from werkzeug.utils import secure_filename

BASE_URL = 'http://127.0.0.1:5000/'
UPLOADS_URL = BASE_URL + 'content/'

UPLOAD_FOLDER = os.getcwd() + '\\content\\'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello():
    return 'My first flask app <a href="/about">About</a>'
	
@app.route('/about/')
def about():
	str = url_for('about')
	return 'About Us at %s' % str

@app.route('/profile/<profile_name>')
def profile(profile_name):
	return 'Viewing user: %s' % profile_name

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        # access variables
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        pic = '/uploads/' + upload_file()

        return '<h4>Registered</h4><p>' + name + ' (' + email + ') </p> <img src=' + pic + ' width="200px" /> <p>' + password + '</p>'

    else:
        return render_template('register.html')

def upload_file():
    if request.method == 'POST':
        f = request.files['pic']
        f.save(UPLOAD_FOLDER + secure_filename(uuid.uuid4().hex))

        return f.filename

@app.route('/uploads/<filename>')
def get_upload_url(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# run app
if __name__ == '__main__':
    app.run(debug=True)
