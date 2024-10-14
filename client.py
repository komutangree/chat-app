import socketio

sio = socketio.Client()

sio.connect('https://alexanderdepooter.eu.pythonanywhere.com/')

@sio.on('receive_message')
def on_message(data):
    print(f"Message from server: {data['message']}")

message = input("Enter a message to send: ")
sio.emit('send_message', {'message': message})

sio.wait()
