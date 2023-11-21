#11.Create a real-time chat application using Flask-SocketIO.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index1():
    return render_template('index1.html')

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    emit('message', message, broadcast=True)


if __name__=='__main__':
    app.run(host='0.0.0.0')