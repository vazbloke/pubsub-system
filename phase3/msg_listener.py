# first of all import the socket library
import socket
import pickle
import _thread
from broker import Broker

# next create a socket object
s = socket.socket()
print("Socket successfully created")
port = 12345
s.bind(('', port))
s.listen(5)

broker = Broker()


while True:

    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    order = c.recv(1024)
    message = pickle.loads(order)
    _thread.start_new_thread(broker.process_message, (message,addr))


# Close the connection with the client
c.close()
