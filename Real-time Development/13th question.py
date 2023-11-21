#13. Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template,request
from flask_socketio import SocketIO, emit
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

active_users = set()

@app.route('/')
def index2():
    return render_template('index2.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    active_users.add(request.sid)
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    active_users.remove(request.sid)
    print('Client disconnected')

def send_notification():
    while True:
        if active_users:
            notification = f'Update occurred at {time.strftime("%H:%M:%S")}'
            socketio.emit('notification', notification, namespace='/test')
        time.sleep(5)  # Checking for updates every 5 seconds

if __name__ == '__main__':
    socketio.start_background_task(target=send_notification)
    app.run(host='0.0.0.0')
