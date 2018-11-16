import os
import message_utility as msg_util
from publish import Publish
from db import DB
import subprocess
from msg_sender import Messenger
from log import log_to_file

NEIGHBORS = os.environ["NEIGHBORS"]
BROKER_NAME = os.environ['BROKER_NAME']
log_to_file("Broker ID"+ BROKER_NAME)


class Broker:
    """
    Broker performs tasks as accept subscribe and publish request.  
    """
    def __init__(self):
        self.publish = Publish()
        self.db = DB()
        self.db.create_table_if_not_exists(BROKER_NAME)
        self.neighbour = {}
        self.publish_history = []
        self.set_network_table_list()

    # ------------ network table -----------------------------------
    def set_network_table_list(self, file_name="neighbours.txt"):
        self.neighbour = {}
        """
        with open(os.path.join('info',file_name), 'r') as f:
            for line in f.readlines():
                ip = line.split(";")[0].strip()
                self.neighbour[ip] = []#line.split(";")[1:]
        """
        for nei in NEIGHBORS.split(","):
            self.neighbour[nei]=[]
        return self.neighbour

    def update_neighbour_table(self, neighbour, event):
        if neighbour in self.neighbour.keys() and event not in self.neighbour[event]:
            self.neighbour[neighbour].append(event)

    # ------------ publish function -------------------------------------------------

    def match_and_notify_subscriber(self, message, addr):
        if message.id not in self.publish_history:
            self.publish.notify(message.event, message.message, BROKER_NAME)
            self.match_events_broker(message, addr)
            self.publish_history.append(message.id)
        else:
            log_to_file("already published")

    def match_events_broker(self, msg, addr):
        ms = Messenger()
        for neighbour_ip in self.neighbour:
            if neighbour_ip != addr[0] :#and addr[0] in self.neighbour.keys() and msg.event in self.neighbour[neighbour_ip]:
                log_to_file(str(neighbour_ip)+ "!="+str( addr[0]))
                ms.send_message(msg, neighbour_ip)

    # ----------- subscriber function--------------------------------
    def add_subscriber(self, msg, addr):
        if msg.ttl == 1:
            self.db.add_subscriber(msg.subscriber, msg.event, BROKER_NAME)
            #self.send_subscriber_to_neighbour(msg)
        else:
            for event in msg.event.split(';'):
                if event.strip() == "":
                    continue
                if addr[0] in self.neighbour.keys() and event not in self.neighbour[addr[0]]:
                    self.neighbour[addr[0]].append(event)

    def send_subscriber_to_neighbour(self, msg):
        msg.ttl = 0
        ms = Messenger()
        for neighbour in self.neighbour:
            ms.send_message(msg_util,neighbour)

    # -------------- actions -----------------------------------
    def process_message(self, msg, addr):
        log_to_file(str(msg.__dict__))
        if msg.action == msg_util.SUBSCRIBE:
            self.add_subscriber(msg, addr)
        elif msg.action == msg_util.PUBLISH:
            self.match_and_notify_subscriber(msg, addr)
        elif msg.action == "show":
            ls = self.db.get_mail_list_for_event(msg.event, BROKER_NAME)
            log_to_file("".join(ls))
        elif msg.action == "neighbours":
            log_to_file(str(self.neighbour))
        else:
            log_to_file("not identifies"+str( msg.__dict__))

