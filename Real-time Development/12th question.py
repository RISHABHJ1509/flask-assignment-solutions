#12. Build a Flask app that updates data in real-time using WebSocket connections.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def background_thread():
    while True:
        socketio.sleep(2)  # Update every 2 seconds
        data = {
            'value': random.randint(1, 100),
            'timestamp': time.strftime('%H:%M:%S')
        }
        socketio.emit('update', data, namespace='/test')

@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.start_background_task(target=background_thread)
    app.run(host='0.0.0.0')

