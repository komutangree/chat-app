#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


while True:
    sndmsg = input("Send a Message:\n")
    print("Sending...") 
    socket.send(bytes(f"{sndmsg}"))

    #  Get the reply.
    rcvmessage = socket.recv()
    print("Received reply", rcvmessage)