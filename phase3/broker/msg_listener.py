# first of all import the socket library
import socket, os
import pickle
import _thread
from broker import Broker
from log import log_to_file
"""
Listener demon: listens to message continuouly 
"""

s = socket.socket()
# print("Socket successfully created")
port = 12345
s.bind(('', port))
s.listen(5)

broker = Broker()

log_to_file("Broker started")
print("Broker started.")


while True:

    # Establish connection with client.
    c, addr = s.accept()
    log_to_file('Got connection from'+str(addr))
    print("Got connection from " + str(addr))
    order = c.recv(1024)
    message = pickle.loads(order)
    _thread.start_new_thread(broker.process_message, (message,addr))


# Close the connection with the client
c.close()
