import os

from flask import Flask, url_for, request, render_template
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
        pic = upload_file()

        return '<h4>Registered</h4><p>' + name + ' (' + email + ') </p> <img src='+ pic +' /> <p>' + password + '</p>'

    else:
        return render_template('register.html')

def upload_file():

    if request.method == 'POST':
        f = request.files['pic']
        f.save(UPLOAD_FOLDER + secure_filename(f.filename))

        return UPLOADS_URL + f.filename


# run app
if __name__ == '__main__':
    app.run(debug=True)