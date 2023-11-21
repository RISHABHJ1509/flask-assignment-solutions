#6. Build a Flask app that allows users to upload files and display them on the website.

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index1():
    # Geting the list of files in the upload folder
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index1.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return redirect(request.url)
        if file:
            # Save the uploaded file to the upload folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('index1'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
