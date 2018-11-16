import time

SUBSCRIBE = "subscribe"
PUBLISH = "publish"


class Message:
    """
    Object of Message class are used to communicate through network
    """
    def __init__(self, action, event, sub=None, message=None,id_=None,ttl=None):
        self.action = action
        self.subscriber = sub
        self.event = event
        self.message = message
        self.id = id_
        self.ttl= ttl


def get_subscriber_msg(event, mail):
    z = event + str(time.time())
    return Message(SUBSCRIBE, event, mail, "", ttl=1)


def get_publish_msg(event, msg):
    z = event + str(time.time())
    return Message(PUBLISH, event, "", msg, id_=z)


