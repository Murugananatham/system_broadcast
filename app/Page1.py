import os
from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename
from flask.helpers import flash



app=Flask(__name__)
app.config['SERVER_NAME']= "localhost:5000"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = 'uploads'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.update(
    #Set the secret key to a sufficiently random value
    SECRET_KEY=os.urandom(24)
)
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
   return render_template("home.html")

@app.route('/email_broadcasting')
def email_broadcasting():
   return render_template("email_broadcasting.html") 

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/email_broadcast', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('login')
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',filename=filename))
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)