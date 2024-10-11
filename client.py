#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
while True:
    sndmsg = input("Send a Message:\n")
    print("Sending...") 
    socket.send(bytes(f"{sndmsg}"))

    #  Get the reply.
    rcvmessage = socket.recv()
    print("Received reply", rcvmessage)