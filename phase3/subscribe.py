import os
from msg_sender import Messenger
from db import DB
from broker_list_manager import BrokerManager
import message_utility


class Subscribe:
    def subscribe(self, subscriber_mail_id, events):
        if os.path.exists("phase3.txt"):
            self.subscribe_phase3(subscriber_mail_id,events)
        else:
            DB().add_subscriber(subscriber_mail_id, events)

    def subscribe_phase3(self, subscriber_mail_id, events):
        broker_ip = BrokerManager().get_random_broker()
        msg = message_utility.get_subscriber_msg(events, subscriber_mail_id)
        Messenger().send_message(msg, broker_ip)

    def unsubscribe(self, mail_id, event):
        if not os.path.exists("phase3.txt"):
            DB().remove_subsriber(mail_id, event)
        else:
            # Todo: send delete msg to subscriber
            pass
