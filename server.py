from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print("New client connected")

@socketio.on('send_message')
def handle_message(data):
    print(f"Received message: {data['message']}")
    emit('receive_message', data)
    print("Message sent")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app)