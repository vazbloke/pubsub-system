
ACTIONS=['add','remove','notify']


class Event:
    def __init__(self,action):
        self.action = action


    def add_subscriber(self, mail_id, events):
        for event in events:

