import os
import random
import string
from flask import Flask, render_template, request, redirect, flash, send_from_directory, url_for

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads/")
UPLOAD_FOLDER = os.path.abspath(UPLOAD_DIR)
print(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'some_really_long_random_string_here'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        flash(filename)
        extension = os.path.splitext(filename)[1]
        filename_rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
        ffile = filename_rand + extension
        print(ffile)
        f.save(app.config['UPLOAD_FOLDER']+'/'+ffile)
        flash('/uploads/'+ffile, "upload")
        return redirect(url_for('index'),'wtf')
    return render_template('index.html')

@app.route("/uploads/<filename>", methods=["GET"])
def get_upload(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
if __name__=='__main__':
    app.run(debug=True)

