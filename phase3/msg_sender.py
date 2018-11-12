# Import socket module
import socket
import pickle
import sys
from message_utility import Message


class Messenger:
    def send_message(self, msg, ip='172.17.0.3', port=12345):
        s = socket.socket()
        s.connect((ip, port))
        obj = pickle.dumps(msg)
        s.send(obj)
        s.close()

    def create_dummy_message(self):
        msg = Message("have fun","stacker")
        return msg

    def send_dummy_msg(self):
        msg = self.create_dummy_message()
        self.send_message(msg)


def main():
    sm = Messenger()
    act = sys.argv[1]
    event = sys.argv[2]
    msg = sys.argv[3]
    sub = sys.argv[4]
    ttl = sys.argv[5]
    ip = sys.argv[6]

    msg = Message(act,event,sub,msg,ttl=ttl)
    print(msg.__dict__,ip)
    sm.send_message(msg,ip)


if __name__ == '__main__':
    main()
