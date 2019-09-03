#! /usr/bin/env python3

"""
This part show you how to
create a socket server
"""

import socket
import sys

serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=9999

serversocket.bind((host,port))

#set the maxinum connection count
serversocket.listen(5)

while True:
    clientsocket,addr=serversocket.accept()

    print("connection address is: {}".format(addr))

    message="welcome to this server!"

    clientsocket.send(message.encode('utf-8'))
    clientsocket.close()



