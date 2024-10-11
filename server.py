#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

log = open("logs.log","a")

while True:
    #  Wait for next request from client
    rcvmessage = socket.recv()
    print("Received request:" , rcvmessage)

    #  Do some 'work'
    log.write(rcvmessage)
    sendmsg = input("Send a Message:")

    #  Send reply back to client
    socket.send(bytes(f"{sendmsg}"))