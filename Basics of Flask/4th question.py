#4. Create a Flask app with a form that accepts user input and displays it.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    dob = request.form['dob']
    return render_template('index1.html', username=username, dob=dob)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
