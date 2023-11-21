#5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session

app = Flask(__name__)

# Configure the app to use Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


user_data = {
    'user1': {'name': 'rishabh', 'email': 'jaiswalrishabh1509@gmail.com'},
    'user2': {'name': 'raina', 'email': 'raina22@gmail.com'}
}

@app.route('/')
def index():
    if 'username' in session:
        # If user is logged in, display their data
        username = session['username']
        user_info = user_data.get(username)
        return render_template('profile.html', user_info=user_info)
    # If user is not logged in, redirect to login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in user_data:
            # Store username in session
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    # Remove username from session if it exists
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')



